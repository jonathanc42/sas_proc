def proc_power(mean_diff, std, size=100, alpha=0.05, desired_power=0.8, side='two-sided'):
    """
    calculate the power for a given mean difference and std. the function plots a graph showing the comparison between desired mean differences
    :param mean_diff: the desired mean difference
    :param std: the std value
    :param size: the total sample size. it only consider obs 1 and 2 are having same number of samples
    :param alpha: alpha default value is 0.05
    :param desired_power: will use this value in order to mark on the graph
    :return: the desired size for desired power
    """

    from statsmodels.stats.power import  tt_ind_solve_power
    from scipy.interpolate import interp1d
    import matplotlib.pyplot as plt
    

    fig, ax = plt.subplots()
    effect_size = mean_diff / std

    powers = []

    sizes = range(4, size+1, 2)
    for sample2_size in sizes:
        n = tt_ind_solve_power(effect_size=effect_size, nobs1=sample2_size/2, alpha=alpha, ratio=1.0, alternative=side)
        powers.append(n)

    plt.title('Power vs. Sample Size')
    plt.xlabel('Sample Size')
    plt.ylabel('Power')
    plt.ylim(0,1)
    plt.xlim(0,size)

#         plt.plot(sizes, powers, label='diff={:2.0f}%'.format(100*mean_diff_percent)) #, '-gD')
    plt.plot(sizes, powers) #, '-gD')
    
    try: # mark the desired power on the graph
        # print(len(powers), len(sizes))        
        z1 = interp1d(powers, sizes)
        results = z1(desired_power)

        plt.plot([results], [desired_power], 'gD')
        plt.hlines(y=desired_power,xmin=0,xmax=results,linestyle='--', alpha=0.5)
        plt.vlines(x=results, ymin=0, ymax=desired_power,linestyle='--', alpha=0.5)
        print(results)
        
    except Exception as e:
        print("Error: ", e)
        #ignore

#     plt.legend()
    plt.show()
    # return(int(results))