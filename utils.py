import numpy as np
import torch
import matplotlib.pyplot as plt


def plot_results(data):

    N = 20
    conv_data = data[1000:]
    avg_score = np.mean(conv_data)
    smooth_data = np.convolve(data, np.ones(N)/N, mode='valid')
    t = np.linspace(0,len(data),len(data))

    x_vals = [1000,1000]
    y_vals = [-4,28]

    mean_x_vals = [0,2000]
    mean_y_vals = [avg_score,avg_score]

    plt.figure()
    plt.xlim([0,2000])
    plt.ylim([-2,28])
    plt.plot(data, label='raw data')
    plt.plot(smooth_data, label='running average')
    plt.plot(x_vals, y_vals, color='black', linestyle='--', label='environment solved')
    plt.plot(mean_x_vals, mean_y_vals, color='orange', linestyle='--', label='mean score')
    plt.legend()
    plt.show()
    plt.close()
    
    return



def save_model_params(i_episode, agent, scores):
    """
    
    """
    torch.save({
        'i_episode': i_episode,
        'local_qnetwork_state_dict': agent.qnetwork_local.state_dict(),
        'target_qnetwork_state_dict': agent.qnetwork_target.state_dict(),
        'optimizer_state_dict': agent.optimizer.state_dict(),
        'scores': scores,
        }, 'all_state_dicts.pt')
 
    return
