import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/workspace/week06_slam_localization/ros2_ws/install/course_slam_tools'
