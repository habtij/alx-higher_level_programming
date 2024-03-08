#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  let i = 0;
  while ((len - i) > 0) {
    const temp = list[len];
    list[i] = temp;
    i++;
    len--;
  }
  return list;
};
