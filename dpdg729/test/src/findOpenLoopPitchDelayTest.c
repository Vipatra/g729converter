/*
 * Copyright (c) 2011-2019 Belledonne Communications SARL.
 *
 * This file is part of bcg729.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
/*****************************************************************************/
/*                                                                           */
/* Test Program for find open loop pitch delay bloc                          */
/*     - input : 143+80 weighted Input Speech                                */
/*     - output : the open loop pitch delay in range [20, 143]               */
/*                                                                           */
/*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include "typedef.h"
#include "codecParameters.h"

#include "testUtils.h"

#include "findOpenLoopPitchDelay.h"

int main(int argc, char *argv[] )
{
	/*** get calling argument ***/
  	char *filePrefix;
	getArgument(argc, argv, &filePrefix); /* check argument and set filePrefix if needed */

	/*** input and output file pointers ***/
	FILE *fpInput;
	FILE *fpOutput;

	/*** input and output buffers ***/
	word16_t inputBuffer[MAXIMUM_INT_PITCH_DELAY+L_FRAME]; /* 40 values in Q0 */

	/*** inits ***/
	/* open the input file */
	if ( (fpInput = fopen(argv[1], "rb")) == NULL) {
		printf("%s - Error: can't open file  %s\n", argv[0], argv[1]);
		exit(-1);
	}

	/* create the output file(filename is the same than input file with the .out extension) */
	char *outputFile = malloc((strlen(filePrefix)+5)*sizeof(char));
	sprintf(outputFile, "%s.out",filePrefix);
	if ( (fpOutput = fopen(outputFile, "wb")) == NULL) {
		printf("%s - Error: can't create file  %s\n", argv[0], outputFile);
		exit(-1);
	}
	
	/*** init of the tested bloc ***/

	/*** initialisation complete ***/


	/*** loop over input file ***/
	while(1) /* infinite loop, escape condition is in the reading of data */
	{
		int i;
		/* read the input data until we have some */
		if (fscanf(fpInput,"%hd",&(inputBuffer[0])) != 1) break;
		for (i=1; i<MAXIMUM_INT_PITCH_DELAY+L_FRAME; i++) {
			if (fscanf(fpInput,",%hd",&(inputBuffer[i])) != 1) break;
		}


		/* call the openLoopPitchDelay function, input buffer is accessed in range [-MAXIMUM_INT_PITCH_DELAY, L_FRAME] */
		int openLoopPitchDelay = findOpenLoopPitchDelay(&(inputBuffer[MAXIMUM_INT_PITCH_DELAY]));

		/* write the output to the output file */
		fprintf(fpOutput,"%d\n", openLoopPitchDelay);
	}
	exit (0);
}

