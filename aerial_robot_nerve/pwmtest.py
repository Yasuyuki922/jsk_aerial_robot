#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

def pwm_sequence_publisher():
    pub = rospy.Publisher('/pwm_test', Float32, queue_size=10)
    rospy.init_node('pwm_sequence_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz

#PWM対応表
    pwm_values = {
        'E': 0.656, #329.63
        'F': 0.678, #369.99
        'G': 0.707, #415.30
        'A': 0.722, #440.00
        'B': 0.755, #493.88
        'C': 0.790, #554.37
        'D': 0.806, #587.33
        'E5': 0.842, #659.26
    }

    def publish_pwm_by_name(name, duration_sec):
        if name not in pwm_values:
            rospy.logwarn("Unknown PWM name: %s", name)
            return
        value = pwm_values[name]
        msg = Float32()
        msg.data = value
        start_time = rospy.Time.now()
        duration = rospy.Duration(duration_sec)
        while rospy.Time.now() - start_time < duration and not rospy.is_shutdown():
            rospy.loginfo("Publishing PWM (%s): %.2f", name, value)
            pub.publish(msg)
            rate.sleep()

#入力内容
    publish_pwm_by_name('E', 0.5)
    rospy.sleep(0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('F', 1.0)
    publish_pwm_by_name('E', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('G', 1.0)

    rospy.sleep(1.0)

    publish_pwm_by_name('E', 0.5)
    rospy.sleep(0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('F', 1.0)
    publish_pwm_by_name('E', 1.0)
    publish_pwm_by_name('B', 1.0)
    publish_pwm_by_name('A', 1.0)

    rospy.sleep(1.0)

    publish_pwm_by_name('E', 0.5)
    rospy.sleep(0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('E2', 1.0)
    publish_pwm_by_name('C', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('G', 1.0)
    publish_pwm_by_name('F', 1.5)

    rospy.sleep(1.0)

    publish_pwm_by_name('D', 0.5)
    rospy.sleep(0.25)
    publish_pwm_by_name('D', 0.25)
    publish_pwm_by_name('C', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('B', 1.0)
    publish_pwm_by_name('A', 1.0)

if __name__ == '__main__':
    try:
        pwm_sequence_publisher()
    except rospy.ROSInterruptException:
        pass

    
