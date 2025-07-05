import time
import os
import sys
import subprocess
import threading


class PrintUtils():
    
    @staticmethod
    def print_delay(data,delay=0.03,end="\n"):
        PrintUtils.print_text("\033[37m",end="")
        for d in data:
            d = d.encode("utf-8").decode("utf-8")
            PrintUtils.print_text("{}".format(d),end="",flush=True)
            time.sleep(delay)
        PrintUtils.print_text(end=end)

    @staticmethod
    def print_text(values="",end="\n",flush= False):
        print(values,end=str(end),flush=flush) # force to string

    @staticmethod
    def print_info(data,end="\n"):
        PrintUtils.print_text("\033[37m{}".format(data),end=end)

class Task():
    """
    - type: 任务类型
    - params: 任务参数
    - result: 任务执行结果
    - progress: 任务执行进度
    - timeout: 任务超时时间 
    - subtask: 子任务
    """
    TASK_TYPE_CMD = 0
    TASK_TYPE_CHOOSE = 1
    TASK_TYPE_PATTERN= 2
    def __init__(self,type) -> None:
        self.type = Task.TASK_TYPE_CMD 
    def run(self):
        pass

class Progress():
    import shutil

    # 获取终端的行宽
    terminal_size = shutil.get_terminal_size()
    line_width = terminal_size.columns

    def __init__(self,timeout=10,scale=20) -> None:
        self.timeout = timeout
        self.start = time.perf_counter()
        self.dur  = time.perf_counter() -self.start 
        self.scale = scale
        self.i = 0
        self.latest_log = ""

    def update(self,log=""):
        if (self.i%4) == 0: 
            PrintUtils.print_text('\r[/][{:.2f}s] {}'.format(self.dur,log),end="")
        elif(self.i%4) == 1: 
            PrintUtils.print_text('\r[\\][{:.2f}s] {}'.format(self.dur,log),end="")
        elif (self.i%4) == 2: 
            PrintUtils.print_text('\r[|][{:.2f}s] {}'.format(self.dur,log),end="")
        elif (self.i%4) == 3: 
            PrintUtils.print_text('\r[-][{:.2f}s] {}'.format(self.dur,log),end="")
        sys.stdout.flush()
        self.i += 1
        # update time
        self.latest_log = log
        self.dur  = time.perf_counter() -self.start 

    def update_time(self):
        log = self.latest_log
        if (self.i%4) == 0: 
            print('\r[/][{:.2f}s] {}'.format(self.dur,log),end="")
        elif(self.i%4) == 1: 
            print('\r[\\][{:.2f}s] {}'.format(self.dur,log),end="")
        elif (self.i%4) == 2: 
            print('\r[|][{:.2f}s] {}'.format(self.dur,log),end="")
        elif (self.i%4) == 3: 
            print('\r[-][{:.2f}s] {}'.format(self.dur,log),end="")
        sys.stdout.flush()
        self.dur  = time.perf_counter() -self.start 


    def finsh(self,log="",color='\033[32m'):
        log = log+" "*(Progress.line_width-len(log)-15) 
        PrintUtils.print_text('\r{}[-][{:.2f}s] {}'.format(color,self.dur, log), end="\r\n\r\n")

class CmdTask(Task):
    def __init__(self,command,timeout=0,groups=False,os_command=False,path=None,executable='/bin/sh') -> None:
        super().__init__(Task.TASK_TYPE_CMD)
        self.command = command
        self.timeout = timeout
        self.os_command = os_command
        self.cwd = path
        self.executable = executable

    def getlog(self,callback=None):
        stdout_line = ""
        for line in iter(self.sub.stdout.readline,'b'):
            line = line.rstrip()#.decode('utf8', errors="ignore")
            if callback and line:
                callback(line,'out')
            if(subprocess.Popen.poll(self.sub) is not None):
                if(line==""):
                    break

        for line in iter(self.sub.stderr.readline,'b'):
            line = line.rstrip()#.decode('utf8', errors="ignore")
            if callback and line:
                callback(line,'err')
            if(subprocess.Popen.poll(self.sub) is not None):
                if(line==""):
                    break

    def getlogs(self):
        out = []
        lines = self.sub.stdout.readlines()
        for line in lines:
            line = line.decode("utf-8", errors="ignore").strip()
            if line:
                out.append(line)
            time.sleep(0.001)
        lines = self.sub.stderr.readlines()
        for line in lines:
            line = line.decode("utf-8", errors="ignore").strip()
            if line:
                out.append(line)
            time.sleep(0.001)

        logstr = ""
        for log in out:
            logstr += log
        return logstr


    def command_thread(self,executable='/bin/sh'):
        self.ret_ok = False
        out,err = [],[]
        self.sub = subprocess.Popen(self.command,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd=self.cwd,
                                    shell=True,
                                    bufsize=1,  # Line buffered
                                    universal_newlines=True)
        self.bar = Progress()
        err = []
        out = []
        def log_callback(log,log_type):
            self.bar.update(log)
            if log_type=='out':
                out.append(log)
            else:
                err.append(log)

        self.getlog(log_callback)
        code = self.sub.returncode

        msg = 'code:{}'.format(code)
        if code == 0: msg="success"
        self.ret_code = code

        if code==0:
            self.bar.finsh('CMD Result:{}'.format(msg),'\033[37m')
        else:
            self.bar.finsh('CMD Result:{}'.format(msg),'\033[31m')


        self.ret_out = out
        self.ret_err = err
        self.ret_ok = True

    def run_command(self,executable='/bin/sh'):
        self.command_thread = threading.Thread(target=self.command_thread)
        self.command_thread.start()
        time.sleep(0.5) # 等待线程启动
        while self.is_command_finish()==-1:
            self.bar.update_time()
            time.sleep(0.1)

        start_time = time.time()
        while not self.ret_ok and time.time()-start_time < 2.0: # 2s timeout wait  command_thread end
            time.sleep(0.1)

        # Tracking.put_cmd_result(self.ret_code,self.ret_out,self.ret_err,self.command)
        return (self.ret_code,self.ret_out,self.ret_err)

    def is_command_finish(self):
        # poll 是返回码
        if self.sub.poll() == None:
            return -1
        return self.sub.poll()

    def run_os_command(self):
        """
        退出即结束
        """
        if self.cwd is not None:
            os.system("cd {} && {}".format(self.cwd,self.command))
        else:
            os.system(self.command)

    def run(self):
        PrintUtils.print_info("\033[32mRun CMD Task:[{}]".format(self.command))
        if self.os_command:
            return self.run_os_command()
        return self.run_command()
    
