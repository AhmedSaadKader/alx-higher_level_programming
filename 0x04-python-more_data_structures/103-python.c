#include <stdio.h>
#include <string.h>
#include "Python.h"

/**
 * print_python_bytes - prints some basic infor about bytes objects
 * @p: byte object
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b;
	long unsigned int i = 0;

	b = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("size: %ld\n", b->ob_base.ob_size);
	printf("trying string: %s\n", b->ob_sval);
	if (strlen(b->ob_sval) > 10)
		printf("first 10 bytes = ");
	else
		printf("first %ld bytes = ", strlen(b->ob_sval) + 1);
	while (i <= strlen(b->ob_sval) && i < 10)
	{
		printf("%02hhx ", b->ob_sval[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - prints some basic info about python lists
 * @p: python list
*/

void print_python_list(PyObject *p)
{
	PyListObject *list;
	const char *type;
	int i = 0;

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	while (i < list->ob_base.ob_size)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
		i++;
	}
}

