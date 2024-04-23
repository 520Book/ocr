/**
  * 识别验证码的小工具，仅支持识别英文字母和数字.
  * @param base64Str is the picture's base64 string.
  * eg: 
  *     import { encodeBase64 } from "https://deno.land/std@0.223.0/encoding/base64.ts";
  *     let imageU8Arr = Deno.readFileSync('./code.jpg');
  *     let base64Str = encodeBase64(imageU8Arr);
  */
export async function ocr(base64Str: string):Promise<string> {
  try {
    let p = Deno.run({
      cmd: ['python', './ocr.py', base64Str],
      stdout: 'piped'
    })
    let pout = await p.output();  
    let code = new TextDecoder('utf-8').decode(pout);
    return code;
  } catch(e) {
    console.log('Did you install python?\n\n', e);
    return '';
  }
}