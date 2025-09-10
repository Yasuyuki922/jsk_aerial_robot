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
        'D4s': 0.642,
        'F4s': 0.677,
        'G4': 0.704,
        
        'A4s': 0.739,
        'B4': 0.755,

        'C5s': 0.799,
        'D5s': 0.854,
        'E5': 0.898,  
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

    publish_pwm_by_name('D5s', 0.25)
    publish_pwm_by_name('C5s', 0.15)
    publish_pwm_by_name('B4', 0.15)
    publish_pwm_by_name('C5s', 0.15)
    
    publish_pwm_by_name('C5s', 0.30)
    publish_pwm_by_name('D5s',0.30)
    publish_pwm_by_name('end',0.60)

    publish_pwm_by_name('end',0.60)    
    publish_pwm_by_name('D5s', 0.15)
    publish_pwm_by_name('C5s', 0.15)
    publish_pwm_by_name('B4', 0.15)
    publish_pwm_by_name('C5s', 0.15)
    
    publish_pwm_by_name('C5s', 0.30)
    publish_pwm_by_name('D5s', 0.30)
    publish_pwm_by_name('E5', 0.30)
    publish_pwm_by_name('D5s', 0.30)

    publish_pwm_by_name('D5s', 0.30)                                                                
    publish_pwm_by_name('A4s', 0.20)
    publish_pwm_by_name('end', 0.10)
    publish_pwm_by_name('A4s', 0.20)
    publish_pwm_by_name('end', 0.10)
    publish_pwm_by_name('A4s', 0.30)

    publish_pwm_by_name('A4s', 0.30)
    publish_pwm_by_name('B4', 0.30)
    publish_pwm_by_name('end', 0.30)
    publish_pwm_by_name('D4s', 0.30)
    
    publish_pwm_by_name('end', 1.20)
    
    publish_pwm_by_name('D5s', 0.30)                                                                
    publish_pwm_by_name('C5s', 0.15)
    publish_pwm_by_name('B4', 0.15)
    publish_pwm_by_name('B4', 0.30)
    publish_pwm_by_name('C5s', 0.30)

    publish_pwm_by_name('D5s', 0.30)
    publish_pwm_by_name('C5s', 0.30)
    publish_pwm_by_name('E5', 0.30)
    publish_pwm_by_name('D5s', 0.20)
    publish_pwm_by_name('end', 0.10)

    publish_pwm_by_name('D5s', 0.60)
    publish_pwm_by_name('end', 0.60)

    publish_pwm_by_name('end', 0.50)
    publish_pwm_by_name('D5s', 0.25)
    publish_pwm_by_name('C5s', 0.15)
    publish_pwm_by_name('B4', 0.15)
    publish_pwm_by_name('C5s', 0.15)

    publish_pwm_by_name('C5s', 0.30)
    publish_pwm_by_name('D5s',0.30)
    publish_pwm_by_name('E5', 0.30)
    publish_pwm_by_name('D5s',0.20)
    publish_pwm_by_name('end',0.10)

    publish_pwm_by_name('D5s', 0.30)
    publish_pwm_by_name('A4s', 0.20)
    publish_pwm_by_name('end', 0.10)
    publish_pwm_by_name('A4s', 0.20)
    publish_pwm_by_name('end', 0.10)
    publish_pwm_by_name('A4s', 0.30)

    publish_pwm_by_name('A4s', 0.30)
    publish_pwm_by_name('B4', 0.30)
    publish_pwm_by_name('end', 0.30)
    publish_pwm_by_name('D4s', 0.30)


    publish_pwm_by_name('end',0.90) 
    publish_pwm_by_name('C5s', 0.30)
                             
    publish_pwm_by_name('D5s', 0.30)       
    publish_pwm_by_name('C5s', 0.15)
    publish_pwm_by_name('B4', 0.15)                             
    publish_pwm_by_name('B4', 0.30)         
    publish_pwm_by_name('A4', 0.15)             
    publish_pwm_by_name('G4', 0.15)
    
    publish_pwm_by_name('G4', 0.30)                                                
    publish_pwm_by_name('end', 0.90)
    
    publish_pwm_by_name('end', 1.20)
    
    publish_pwm_by_name('G4', 0.30)                  
    publish_pwm_by_name('end', 0.30)                                  
    publish_pwm_by_name('G4', 0.30)     
    publish_pwm_by_name('end', 0.15)             
    publish_pwm_by_name('F4s', 0.15)
    
    publish_pwm_by_name('G4', 0.15)                                           
    publish_pwm_by_name('D5s', 0.45)                                                  
    publish_pwm_by_name('end', 0.60)
    
    publish_pwm_by_name('end', 0.90)                                       
    publish_pwm_by_name('C5s', 0.15)                                         
    publish_pwm_by_name('D5s', 0.30)                                      
    publish_pwm_by_name('C5s', 0.30)                                             
    #publish_pwm_by_name('F5s', 0.30)        


    publish_pwm_by_name('end', 20.0)

if __name__ == '__main__':
    try:
        pwm_sequence_publisher()
    except rospy.ROSInterruptException:
        pass
