#!/usr/bin/node
exports.esrever = function (list) {
  new_list = [];
  for (let i = 0; i < list.length; i++) {
    const element = list[i];
    new_list.unshift(element);
  }
  return new_list;
};
