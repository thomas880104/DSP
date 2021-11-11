def genChirpSignal(
    T=  1,    
    f0=  440,
    f1=  880,
    style= 'linear', 
    A=  1,    
    sr= 44100 
    ):
    '''
    input
    ---------
    T = sec
    style = ['linear','exponential','sinusoidal','square','sawtooth']
    A = amplitude
    sr = Hz, sampling rate, samples/sec

    output
    ----------
    sr = sample rate
    ys = wave array
    '''


    # specify the time-series for the given duration
    ts= np.linspace(0, T, sr*T)
    
    #
    # specify the freq as fs= f(ts), 
    #
    # f() can be any function, 
    # boundary conditions 
    # f(t0)==f0
    # f(t1)==f1
    #

    # linear
    def linear_style(ts):       
        fs= f0 + (f1-f0)/T * ts  
        return fs
    
    # exponential
    def exponential_style(ts):       
        fs= f0 * (f1/f0)**(ts/T)  
        return fs
    
    # sinusoid for 3 periods
    def sinusoidal_style(ts):       
        fs= (f1-f0)*(1 + np.sin(2 * π * ts/T*3)) 
        return fs
    
    # square
    def square_style(ts):       
        fs= f0 + (f1-f0)/T**2 * ts**2  
        return fs
    
    # sawtooth
    def sawtooth_style(ts):       
        frac, _= np.modf(ts)
        fs= frac*(f1-f0)+f0
        return fs
    
    # if chosen style is not in the list 
    def unknown_style(ts, T0=1):       
        fs= np.random.random(len(ts))*(f1-f0)+f0
        return fs

    # choose style
    if style in ['linear', 'lin', 'l', 'L']:   
        fs= linear_style(ts)
    elif style in ['exponential', 'exp', 'e', 'E']:   
        fs= exponential_style(ts)
    elif style in ['sinusoidal', 'sin', 's', 'S']: 
        fs= sinusoidal_style(ts)
    elif style in ['square', 'squ', 'sq', 'SQ']:   
        fs= square_style(ts)
    elif style in ['sawtooth', 'saw', 'sa', 'SA']:   
        fs= sawtooth_style(ts)
    else:
        print('style unknown')
        fs= unknown_style(ts)

    # radian frequency
    ws= 2*π*fs
    
    # θ = Integrate (w(t) dt)
    dt=  T/len(ts)
    θ =  np.cumsum(ws)*dt  # this is mimic the integration 
    
    # finally, generate the signal
    ys= A * np.sin(θ)
    
    return sr, ys