//============================================================================================
//	LocCrabs
//============================================================================================

#ifndef _LocCrabs_h_
#define _LocCrabs_h_

#include "..\common_h\vmodule_api.h"
#include "..\common_h\matrix.h"
#include "..\common_h\dx8render.h"
#include "..\common_h\collide.h"

#include "LocCrab.h"


class LocCrabs : public ENTITY  
{
public:
	LocCrabs();
	virtual ~LocCrabs();

//--------------------------------------------------------------------------------------------
public:
	//�������������
	bool Init();
	//����������
	void Execute(dword delta_time);
	//���������
	void Realize(dword delta_time);

	//���������
	dword _cdecl ProcessMessage(MESSAGE & message);

//--------------------------------------------------------------------------------------------
private:
	LocCrab crab[32];
	long num;
};

#endif

