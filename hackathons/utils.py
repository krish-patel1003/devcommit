import os


def hackathon_image_path(image_type):
    '''
    returns path for different type of hackathon images
    '''
    
    if image_type == "bg":
        return os.path.join('hackathons/bg_imgs/')

    elif image_type == "hack":
        return os.path.join('hackathons/hack/')
    
    else:
        raise ValueError("image type invalid")


def convert_datetime_to_str(datetime):
    '''
    returns datetime object converted in string format 
    '''

    return datetime.strftime("%Y-%m-%d %H:%M:%S")