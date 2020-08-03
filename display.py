#!/bin/bash

import numpy as np
import matplotlib.pyplot as plt


file1_x, file1_y = np.loadtxt("/fslhome/cohenand/training/data/output1.dat", unpack=True)
file2_x, file2_y = np.loadtxt("/fslhome/cohenand/training/data/output2.dat", unpack=True)
file3_x, file3_y = np.loadtxt("/fslhome/cohenand/training/data/output3.dat", unpack=True)
file4_x, file4_y = np.loadtxt("/fslhome/cohenand/training/data/output4.dat", unpack=True)
file5_x, file5_y = np.loadtxt("/fslhome/cohenand/training/data/output5.dat", unpack=True)
file6_x, file6_y = np.loadtxt("/fslhome/cohenand/training/data/output6.dat", unpack=True)
file7_x, file7_y = np.loadtxt("/fslhome/cohenand/training/data/output7.dat", unpack=True)





data = np.zeros([2])

time_step_plot = np.linspace(0,9,100000)
analytical_value = np.zeros(len(time_step_plot))
analytical_value = analytical_value + np.exp(9*-3)

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file1_x, file1_y)
err=np.abs(analytical_value[-1]-file1_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,200,'error = '+str(err)+'%')
plt.savefig("figure1")
plt.show(block=True)

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file2_x, file2_y)
err=np.abs(analytical_value[-1]-file2_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure2")
plt.show()

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file3_x, file3_y)
err=np.abs(analytical_value[-1]-file3_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure3")
plt.show()

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file4_x, file4_y)
err=np.abs(analytical_value[-1]-file4_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure4")
plt.show()

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file5_x, file5_y)
err=np.abs(analytical_value[-1]-file5_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure5")
plt.show()

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file6_x, file6_y)
err=np.abs(analytical_value[-1]-file6_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure6")
plt.show()

plt.figure()
plt.plot(time_step_plot,analytical_value)
plt.plot(file7_x, file7_y)
err=np.abs(analytical_value[-1]-file7_y[-1])/analytical_value[-1]*100
err=round(err,2)
plt.text(.5,.9,'error = '+str(err)+'%')
plt.savefig("figure7")
plt.show()


