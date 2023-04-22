import os


def hackathon_submission_image_path(type):
    '''
    returns path for different type of hackathon submission images
    '''
    
    if type == "image":
        return os.path.join('hackathon_submission/images/')

    elif type == "file":
        return os.path.join('hackathon_submission/files/')
    
    else:
        raise ValueError("image type invalid")