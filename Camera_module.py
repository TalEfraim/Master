import cv2
import Logger_module

def control_camera(on_off):
    if on_off == "on":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            ErrorMsg = 'Failed to open camera.'
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')
            return
        # Read frames from the camera while the camera is on
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Display the frame
            cv2.imshow("Camera", frame)
            # Check if the camera should be turned off
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()
    elif on_off == "off":
        # Close any open camera windows
        cv2.destroyAllWindows()
    else:
        print("Invalid on_off argument. Please specify either 'on' or 'off'.")


