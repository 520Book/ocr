# ocr

识别验证码的小工具。

记住，`ocr`是一个异步函数。

# Examples

first new a ts file named `test.ts`.

```ts
import { encodeBase64 } from "https://deno.land/std@0.223.0/encoding/base64.ts";
import { ocr } from "https://deno.land/x/ocr_by_python/mod.ts";

const image = await Deno.readFile('./1.jpg');
const base64data = encodeBase64(image); 
console.log(await ocr(base64data));
```

then run the below command:
```shell
# install the module
$ deno add @xtool/sleep

# run the test.ts
$ deno run test.ts
```
