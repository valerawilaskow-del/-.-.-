let num = 5;

function func(localNum) {
	console.log(localNum);
}
num = 3;
func(num);