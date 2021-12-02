const J = JSON.parse(require('fs').readFileSync("./inputadv.json", 'utf8')).values;
const L = require('lodash');
function cnt(num){return H.chain(J).map((_,i, r)=>L.sum(L.take(L.slice(r,i),num))).filter((o, i, r) => i > 0 && r[i - 1] < o).value().length};
console.log("1:", cnt(1), "\n2:", cnt(3));