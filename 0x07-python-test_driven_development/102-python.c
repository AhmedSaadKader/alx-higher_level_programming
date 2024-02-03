#include <string.h>
#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - prints Python strings
 * @p: python string
*/

void print_python_string(PyObject *p)
{
	PyUnicodeObject *str;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str = (PyUnicodeObject *)p;
	printf("  type: %s\n", Py_TYPE(str)->tp_name);
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(str));
	printf("  value: %S\n", PyUnicode_AsWideCharString(p, NULL));
}
