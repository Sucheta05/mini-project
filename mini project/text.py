def text_objects(text,font):
    textsurface=font.render(text,True,(255,0,0))
    return textsurface,textsurface.get_rect()