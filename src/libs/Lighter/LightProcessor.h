//============================================================================================
//	Spirenkov Maxim aka Sp-Max Shaman, 2001
//--------------------------------------------------------------------------------------------
//
//--------------------------------------------------------------------------------------------
//	LightProcessor
//--------------------------------------------------------------------------------------------
//
//============================================================================================

#ifndef _LightProcessor_H_
#define _LightProcessor_H_

#include "LGeometry.h"
#include "LighterLights.h"
#include "OctTree.h"
#include "Window.h"

class VDX9RENDER;

class LightProcessor
{
    //--------------------------------------------------------------------------------------------
    //Конструирование, деструктурирование
    //--------------------------------------------------------------------------------------------
  public:
    LightProcessor();
    virtual ~LightProcessor();
    void SetParams(LGeometry *g, Window *win, LighterLights *lit, OctTree *ot, VDX9RENDER *_rs);
    void UpdateLightsParam();

    //Выполнить шаг вычислений
    void Process();

    //--------------------------------------------------------------------------------------------
    //Инкапсуляция
    //--------------------------------------------------------------------------------------------
  private:
    //Расчитать затенения
    void CalcShadows();
    //Сгладить затенённость
    void SmoothShadows();
    //Сгладить освещение
    void BlurLight();
    //Расчитать освещение
    void CalcLights(long lit = -1, bool isCos = true, bool isAtt = true, bool isSdw = true);
    //Распределить затенение с треугольника на вершины
    void ApplyTriangleShadows(Triangle &t);

  private:
    LGeometry *geometry;
    Window *window;
    LighterLights *lights;
    VDX9RENDER *rs;
    OctTree *octtree;

    long shadowTriangle;
    long smoothVertex;
    long blurVertex;
};

#endif
