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
	long unsigned int i = 0, size, bytes_no;

	b = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = b->ob_base.ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", b->ob_sval);
	if (size >= 10)
		bytes_no = 10;
	else
		bytes_no = size + 1;
	printf("  first %ld bytes:", bytes_no);
	while (i <= bytes_no)
	{
		if (b->ob_sval[i] >= 0)
			printf(" %02x", b->ob_sval[i]);
		else
			printf(" %02x", 256 + b->ob_sval[i]);
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
	long int i = 0;

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	while (i < list->ob_base.ob_size)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check(list->ob_item[i]))
		{
			print_python_bytes(list->ob_item[i]);
		}
		i++;
	}
}

