#!/usr/bin/node
const list = require('./100-data').list;
(() => {
  const new_list = list.map((value, index) => {
    return value * index;
  });
  console.log(new_list);
})();
