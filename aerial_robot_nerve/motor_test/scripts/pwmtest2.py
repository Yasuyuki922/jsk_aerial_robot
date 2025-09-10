#!/usr/bin/env python
import rospy
from spinal.msg import PwmTest  # spinalメッセージ型に変更

def pwm_sequence_publisher():
    pub = rospy.Publisher('/pwm_test', PwmTest, queue_size=10)
    rospy.init_node('pwm_sequence_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz

    # PWM対応表
    pwm_values = {
        'E': 0.653,   # 329.63 Hz, E4
        'F': 0.677,   # 369.99 Hz, F#4
        'G': 0.704,   # 415.30 Hz, G#4
        'A': 0.720,   # 440.00 Hz, Aa
        'B': 0.755,   # 493.88 Hz, B4
        'C': 0.799,   # 554.37 Hz, C#4
        'D': 0.828,   # 587.33 Hz, D5
        'E5': 0.898,   # 659.26 Hz, E5
        'end': 0.500, # end
    }

    def publish_pwm_by_name(name, duration_sec, motor_id=0):
        if name not in pwm_values:
            rospy.logwarn("Unknown PWM name: %s", name)
            return
        pwm_value = pwm_values[name]
        msg = PwmTest()
        msg.motor_index = [motor_id]
        msg.pwms = [pwm_value]
        start_time = rospy.Time.now()
        duration = rospy.Duration(duration_sec)
        while rospy.Time.now() - start_time < duration and not rospy.is_shutdown():
            rospy.loginfo("Publishing PWM (%s): %.3f to motor %d", name, pwm_value, motor_id)
            pub.publish(msg)
            rate.sleep()

    publish_pwm_by_name('E', 0.5)
    #rospy.sleep(0.25)
    publish_pwm_by_name('end', 0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('F', 1.0)
    publish_pwm_by_name('E', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('G', 1.0)

    #rospy.sleep(1.0)
    publish_pwm_by_name('end', 1.0)


    publish_pwm_by_name('E', 0.5)
    #rospy.sleep(0.25)
    publish_pwm_by_name('end', 0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('F', 1.0)
    publish_pwm_by_name('E', 1.0)
    publish_pwm_by_name('B', 1.0)
    publish_pwm_by_name('A', 1.0)

    #rospy.sleep(1.0)
    publish_pwm_by_name('end', 1.0)

    publish_pwm_by_name('E', 0.5)
    #rospy.sleep(0.25)
    publish_pwm_by_name('end', 0.25)
    publish_pwm_by_name('E', 0.25)
    publish_pwm_by_name('E5', 1.0)
    publish_pwm_by_name('C', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('G', 1.0)
    publish_pwm_by_name('F', 1.5)

    #rospy.sleep(1.0)
    publish_pwm_by_name('end', 1,0)

    publish_pwm_by_name('D', 0.5)
    #rospy.sleep(0.25)
    publish_pwm_by_name('end', 0.25)
    publish_pwm_by_name('D', 0.25)
    publish_pwm_by_name('C', 1.0)
    publish_pwm_by_name('A', 1.0)
    publish_pwm_by_name('B', 1.0)
    publish_pwm_by_name('A', 1.0)

    publish_pwm_by_name('end', 20.0)

if __name__ == '__main__':
    try:
        pwm_sequence_publisher()
    except rospy.ROSInterruptException:
        pass
