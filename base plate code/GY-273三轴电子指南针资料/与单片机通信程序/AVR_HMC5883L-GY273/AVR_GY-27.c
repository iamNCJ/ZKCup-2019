/*****************************************
* ����AVR��Ƭ��GY-27ģ��ͨ�ų��� 		 *
* HMC5883L+ADXL345 ͨ�ų���              *
* ��    �ܣ�IICͨ�Ŷ�ȡ���ݲ���ʾ        *
* ʱ��Ƶ�ʣ��ڲ�1M 						 *
* ��    �ƣ����˵���					 *
* �޸����ڣ�2011��4��20��				 *
* ���뻷����ICC-AVR7.14					 *
* ʵ�黷����ATmega16+1602    			 *
* ʹ�ö˿ڣ�PC0,PC1,PC6,PC7,PA4~PA7 	 *
* ��    ����Ī����ʵ�����24c02��ȡʵ��  *
*****************************************/
#include <iom16v.h>
#include "I2C.h"
#include "1602.h"
#include "delay.h"
#include  "math.h"  
#include  "stdio.h"  
void conversion(unsigned int i);
unsigned char display[5]={0,0,0,0,0};//��ʾ����

/*********************************************
����ת��,ʮ����������ת����10����
����ʮ�����Ʒ�Χ��0x0000-0x270f��0-9999��
����ֳɸ�ʮ��ǧλ����ascii������ʾ��
**********************************************/
void conversion(unsigned int i)  
{  
 	display[0]=i/10000+0x30 ;
    i=i%10000;    //ȡ������
	display[1]=i/1000+0x30 ;
    i=i%1000;    //ȡ������
    display[2]=i/100+0x30 ;
    i=i%100;    //ȡ������
    display[3]=i/10+0x30 ;
   i=i%10;     //ȡ������
    display[4]=i+0x30;  
}
//*******************************
//��ʾ�Ƕ�
void display_angle(void)
{   float temp;
      int x,y;
	 double angle;

     x=I2C_Read(0x03);
     x=(x<<8)+I2C_Read(0x04);
	 
	 y=I2C_Read(0x07);
     y=(y<<8)+I2C_Read(0x08);
	
	 
     angle= atan2((double)y,(double)x) * (180 / 3.14159265) + 180; // angle in degrees
     angle*=10;

    conversion(angle);          //ת������ʾ��Ҫ������
	LCD_write_char(0,0,'A');   //��0�У���0�� ��ʾA
	LCD_write_char(1,0,'n');   //
	LCD_write_char(2,0,'g');   //
	LCD_write_char(3,0,'l');   //
	LCD_write_char(4,0,'e');   //
    LCD_write_char(5,0,':'); 
    LCD_write_char(6,0,display[1]);  
    LCD_write_char(7,0,display[2]); 
    LCD_write_char(8,0,display[3]); 
    LCD_write_char(9,0,'.'); 
	LCD_write_char(10,0,display[4]); 
	LCD_write_char(11,0,0xdf); 
	
}

/*******************************
������
*******************************/
void main(void)
{	
	unsigned char i;		
	 delay_nms(50);          //lcd�ϵ���ʱ
	 LCD_init();             //lcd��ʼ��
     
	while(1){               //ѭ��  
	I2C_Write(0x02,0x00);   //ģʽ�Ĵ���д0
	delay_nms(50); 
	display_angle();       //��ʾ�Ƕ�
	delay_nms(50); 	
    }
}

