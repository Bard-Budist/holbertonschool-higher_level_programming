#!/usr/bin/node
if (process.argv.length > 3) {
  const args = [];
  for (let i = 2; i < process.argv.length; i++) {
    args.push(process.argv[i]);
  }
  args.sort((a, b) => a - b);
  console.log(args[process.argv.length - 4]);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  console.log(0);
}
