// long reverse_logic(long x, long y, long z)
// {
//     long result;
//     if(x<y){
//         if(x>z){
//             result = z - x;
//         }else{
//             result = z + x;
//         }
//     }else{
//         if(y>z){
//             result = z-y;
//         }else{
//             result = z+y;
//         }
//     }
//     return result;
// }

// long loop(long x, long n)
// {
//  long result = 0;
//  long mask;
//  for (mask = 1; mask != 0 ; mask<<=n) {
//     result |= (mask & x);
//  }
//     return result;
// }

// long loop_while_hw5(long a, long b)
// {
//     long result = 1;
//     while (b<a) {
// 	    result = result + a - b;
// 	    b = b+1;
//     }
//     return result;
// }

void switch_hw5(long a, long b, long c, long *dest)
{
    long val;
    switch(a) {
    case 0:
	    val = c - b;
	break;
    case 1:
	    c = a<<4 + a;
	/* Fall through */
    case 3:
	    val = c^(-1);
	break;
    case 5:
    case 7:
	    val = (c+a)>>4;
	break;
    default:
	    val = a+b;
    }
    return val;
}