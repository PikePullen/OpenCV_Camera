import cv2

cap = cv2.VideoCapture(0)

"""how to write video to object"""
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #there are other frame options
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

"""filename, codec (divx is for windows), fps(20-30 value), (width, height)"""
# windows = *'DIVX'
# linux or max = *'XVID'
writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),20,(width,height))

while True:
    ret, frame = cap.read()

    # writer.write(frame)

    cv2.imshow('my video frame', frame);

    """grayscale video"""
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('my video frame', gray);

    """flip along horiz"""
    # flipImg = cv2.flip(frame, 0)
    # cv2.imshow('my video frame', flipImg);

    """flip along vert"""
    # flipImg = cv2.flip(frame, 1)
    # cv2.imshow('my video frame', flipImg);

    """draw on frame"""
    # drawImg = cv2.rectangle(frame, pt1=(384, 10), pt2=(500, 150), color=(0, 255, 0), thickness=10)
    # cv2.imshow('my video frame', drawImg);

    """threshhold always returns a tuple"""
    # ret, th = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    # cv2.imshow('my video frame', th);

    """blurs image and adds text on top"""
    # font = cv2.FONT_HERSHEY_COMPLEX
    # cv2.putText(frame, text='Pike', org=(10,200), fontFace=font, fontScale=5, color=(255,0,0), thickness=4)
    # bilateral = cv2.bilateralFilter(frame, 9, 75, 75)
    # cv2.imshow('my video frame', frame);

    """Save video files"""
    # writer.write(th)
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()