import math

'''Out of Plane Design for Reinforced Masonry Shear Walls'''

#Find Out-of-Plane Load per ASCE 7-10 12.11.2.1
#Fp = 0.4*Sds*Ie*W
Sds = 0.875
Ie = 1.0 
W = 1.0
Fp = 0.4*Sds*Ie*W
Fp_ASD = 0.7*Fp
'''format and print'''
if True:
    Fp = round(Fp, 4)
    Fp_ASD = round(Fp_ASD, 3)

    print('Fp = ',Fp)
    print('FP_ASD = %s*W' %Fp_ASD)



#Calculate Required Moment 
M_unfactored = 3.0 #K-ft
M_ASD = M_unfactored*Fp_ASD #K-ft
print('M_ASD = %s K-ft' %M_ASD)



#Estimate Required Steel Area by using j_est = 0.9
#If p_est < p_bal = 0.0032, As_est is conservative
Fs = 32000 #psi
j_est = 0.9
d = 3.81 #in
b = 12 #in
As_est = M_ASD * 12 / (Fs*j_est*d) * 1000 #in^2
p_est = As_est / (b*d) 
'''format and print'''
if True:
    As_est = round(As_est, 3)
    p_est = round(p_est, 5)

    print('Fs = %s psi' %Fs)
    print('As_est = %s in^2' %As_est)
    print('p_est = %s' %p_est)

    if p_est <= 0.0032:
        print ('p_est < p_bal = 0.0032, try reinforcement based on p_est')
        print('------------------------------------')
        print()
    else:
        print('Error, re-estimate section')



#Try a reinforcement size and spacing based on p_est
barsize = 'No.5' 
bar_area = 0.31 #in^2
bar_spacing = 32 #in
As = bar_area/bar_spacing*12 #in^2/ft
Es = 29000000 #psi
Em = 900*1500 #psi
n = Es/Em
p = As/b/d
k = math.sqrt(2*p*n + (p*n)**2) - p*n
j = 1 - k/3
'''format and print'''
if True:
    As = round(As, 3)
    n = round(n,2)
    p = round(p,5)
    k = round(k,3)
    j = round(j,3)

    print('Try %s bars @ %s in o.c.' %(barsize, bar_spacing))
    print('As = %s in^2/ft' %As)
    print('n = %s' %n)
    print('p = %s' %p)
    print('k = %s' %k)
    print('j = %s' %j)



#Check Moment capacity of Masonry 
Fb = 0.45*1500
Mm = Fb/2*j*k*b*(d**2)/12/1000 #K-ft
'''format and print'''
if True:
    Mm = round(Mm,3)
    if Mm >= M_ASD:
        print('Mm = %s K-ft > %s K-ft = M_ASD. Section is Adequate' %(Mm, M_ASD))
    else: 
        print('Mm = %s K-ft < %s K-ft = M_ASD. FAILED' %(Mm, M_ASD))



#Check Moment capacity of Steel Reinforcement
Ms = As*Fs*j*d/12/1000 #K-ft
'''format and print'''
if True:
    Ms = round(Ms,3)
    if Ms >= M_ASD:
        print('Ms = %s K-ft > %s K-ft = M_ASD. Section is Adequate' %(Ms, M_ASD))
    else: 
        print('Ms = %s K-ft < %s K-ft = M_ASD. FAILED' %(Ms, M_ASD))













