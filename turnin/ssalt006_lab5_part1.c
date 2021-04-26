/*	Author: Skyler Saltos 
 *  Partner(s) Name: 
 *	Lab Section:22
 *	Assignment: Lab #5  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	//inputs A & B
	DDRA = 0x00;
	PORTA = 0xFF;

	//outputs C
	DDRC = 0xFF;
	PORTC = 0x00;
	
    /* Insert your solution below */


	unsigned char fuelInput;
	unsigned char gasLight;

    while (1) {
	
	    fuelInput = ~PINA & 0x0F;
	    gasLight = 0x00;

	    if(fuelInput == 0x00){

		gasLight = 0x01;

	    }//empty tank

	    else if ( fuelInput <= 0x02 && fuelInput > 0x00 ){
	
		    	PORTC = 0x20;
			gasLight = 0x01;

	    }//fuel input is less than or equal 2
	    	
	    else if ( fuelInput == 0x03 || fuelInput == 0x04 )
	    {
			PORTC = 0x30;
			gasLight = 0x01;

	    }//gas range 
	
	    else if (fuelInput == 0x05 || fuelInput == 0x06 ){

			PORTC = 0x38;


	    }//gas range 


	    else if (fuelInput == 0x07 || fuelInput == 0x08 || fuelInput == 0x09){

			PORTC = 0x3C;

	    }//gas range 


	    else if (fuelInput == 0x0A || fuelInput == 0x0B || fuelInput == 0x0C){

		    	PORTC = 0x3E;

	    }//gas range 


	    else if( fuelInput == 0x0D || fuelInput == 0x0E ||  fuelInput == 0x0F){

			PORTC = 0x3F;


	    }//gas range 



	if(gasLight){

		PORTC = PORTC |  0x40;

	}//set P6 to 1


	
    }
    return 1;
}
