// call_function.c - A sample of calling 
// python functions from C code
// 
#include <Python.h>
#include <iostream>
#include <string>
#include <sstream>

int main(int argc, char *argv[])
{
    // Initialize the Python Interpreter
    Py_Initialize();

    PyRun_SimpleString("import numpy as np\n");
    PyRun_SimpleString("from xgboost.sklearn import XGBClassifier");
    PyRun_SimpleString("sklearn.metrics import accuracy_score");
    PyRun_SimpleString("import time");
    PyRun_SimpleString("import pickle");

    PyObject *pName, *pModule, *pDict, *pFunc;

    wchar_t Path[10] = L"./";
    PySys_SetPath(Path);

    // import essential pakage here
    //PyRun_SimpleString("import numpy\n");

    // Build the name object
    pName = PyUnicode_FromString("WWZZ");

    // Load the module object
    pModule = PyImport_Import(pName);
    std::cout << "La La La .... " << std::endl;

    // pDict is a borrowed reference 
    pDict = PyModule_GetDict(pModule);

    // pFunc is also a borrowed reference 
    pFunc = PyDict_GetItemString(pDict, "main");

    if (PyCallable_Check(pFunc)) 
    {
        PyObject_CallObject(pFunc, NULL);
    } else 
    {
        PyErr_Print();
    }

    // Clean up
    Py_DECREF(pModule);
    Py_DECREF(pName);

    // Finish the Python Interpreter
    Py_Finalize();

    return 0;
}
