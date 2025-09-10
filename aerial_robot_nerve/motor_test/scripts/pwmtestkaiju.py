#!/usr/bin/env python
#kaiju
import rospy
from spinal.msg import PwmTest  # spinalメッセージ型に変更

def pwm_sequence_publisher():
    pub = rospy.Publisher('/pwm_test', PwmTest, queue_size=10)
    rospy.init_node('pwm_sequence_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz

    # PWM対応表
    pwm_values = {
        'D4': 0.633,   # 293.66 Hz, E4
        'D4s': 0.642,  # 311.13 Hz, D4s 
        'F4': 0.663,   # 349.28 Hz, F4
        'G4': 0.693,   # 392.00 Hz, G4

        'C5': 0.777,   # 523.25 Hz, C5
        'D5': 0.828,   # 587.33 Hz, D5 
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

    publish_pwm_by_name('F4', 0.25)
    publish_pwm_by_name('D4s', 0.25)
    publish_pwm_by_name('D4', 0.25)
    publish_pwm_by_name('D4s', 0.25)
    
    publish_pwm_by_name('D4s', 0.50)
    publish_pwm_by_name('F4',0.50)
    publish_pwm_by_name('end',1.0)

    publish_pwm_by_name('end',1.0)    
    publish_pwm_by_name('F4', 0.25)
    publish_pwm_by_name('D4s', 0.25)
    publish_pwm_by_name('D4', 0.25)
    publish_pwm_by_name('D4s', 0.25)
    
    publish_pwm_by_name('D4s', 0.50)
    publish_pwm_by_name('F4', 0.50)
    publish_pwm_by_name('G4', 0.50)
    publish_pwm_by_name('F4', 0.50)
    
    publish_pwm_by_name('F4', 0.50)
    publish_pwm_by_name('C5', 0.50)
    publish_pwm_by_name('C5', 0.50)
    publish_pwm_by_name('C5', 0.50)

    publish_pwm_by_name('C5', 0.50)
    publish_pwm_by_name('D5', 0.50)
    publish_pwm_by_name('end', 0.50)
    publish_pwm_by_name('F4', 0.50)

    publish_pwm_by_name('end', 2.0)

    publish_pwm_by_name('F4', 0.50)
    publish_pwm_by_name('D4s', 0.25)
    publish_pwm_by_name('D4', 0.25)
    publish_pwm_by_name('D4', 0.50)
    publish_pwm_by_name('D4s', 0.50)

    publish_pwm_by_name('F4', 0.50)
    publish_pwm_by_name('D4s', 0.50)
    publish_pwm_by_name('G4', 0.50)
    publish_pwm_by_name('F4', 0.50)

    publish_pwm_by_name('F4', 0.50)
    publish_pwm_by_name('end', 1.50)

    publish_pwm_by_name('end', 20.0)

if __name__ == '__main__':
    try:
        pwm_sequence_publisher()
    except rospy.ROSInterruptException:
        pass
