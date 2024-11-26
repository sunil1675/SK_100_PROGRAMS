#program by SUNIL SIR
#94. Wap with a function which show a progress indicator (ASCII =178)

print('94. Wap with a function which show a progress indicator (ASCII =178) \n ')

import time
for i in range(50):
    print("▓", end='')
    time.sleep(0.1)
print('   COMPLETED!!!!\n')