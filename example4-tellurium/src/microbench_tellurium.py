#!/usr/bin/env python
import microbench
from microbench import *
import psutil
import numpy
import tellurium
import roadrunner
import platform

class MBHostCpuMaxFreq(microbench._NeedsPsUtil):
    """ Capture the number of logical CPU cores """
    def capture_cpu_cores(self, bm_data):
        self._check_psutil()
        bm_data['cpu_freq_max'] = psutil.cpu_freq().max

class MyBench(MicroBench, MBFunctionCall, MBPythonVersion, MBHostInfo, MBHostCpuMaxFreq, MBHostRamTotal):
    outfile = 'microbench_tellurium.json'
    capture_versions = (numpy, tellurium, roadrunner)  # Or use MBGlobalPackages/MBInstalledPackages

    def capture_machine_platform(self, bm_data):
        # Capture platform (i386, x86_64 etc.)
        bm_data['platform'] = platform.machine()
    
mybench = MyBench()


@mybench
def tellurium_lorenz_attractor():
    """
    Tellurium Lorenz Attractor demo

    https://tellurium.readthedocs.io/en/latest/notebooks.html#lorenz-attractor
    """

    r = tellurium.loada ('''
        x' = sigma*(y - x);
        y' = x*(rho - z) - y;
        z' = x*y - beta*z;

        x = 0.96259;  y = 2.07272;  z = 18.65888;

        sigma = 10;  rho = 28; beta = 2.67;
    ''')

    result = r.simulate (0, 20, 1000, ['time', 'x', 'y', 'z'])

tellurium_lorenz_attractor()
