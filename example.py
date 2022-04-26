import pylab as plt

mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySample.append(i)
    myLinear.append(i)
    myQuadratic.append(i*i)
    myCubic.append(i*i*i)
    myExponential.append(1.5**i)

# Same Figure
# plt.plot(mySample, myLinear)
# plt.plot(mySample, myQuadratic)
# plt.plot(mySample, myCubic)
# plt.plot(mySample, myExponential)

# Separate Figures and Adding Labels
plt.figure("linear")
plt.xlabel("sample points")
plt.ylabel("linear function")
plt.plot(mySample, myLinear)

plt.figure("quadratic")
plt.plot(mySample, myQuadratic)

plt.figure("cubic")
plt.plot(mySample, myCubic)

plt.figure("exponential")
plt.plot(mySample, myExponential)

plt.figure("quadratic")
plt.ylabel("quadratic fuction")
plt.title("Sample Outputs For a Quadratic Graph")





plt.show()