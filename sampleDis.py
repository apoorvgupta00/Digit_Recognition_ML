import matplotlib.pyplot as plt

def display_sample(image,label,predicted=999):
    plt.title('Label: %d, Predicted: %d' % (label, predicted))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    
