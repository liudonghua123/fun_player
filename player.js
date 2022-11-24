// ffi not working, installation failed
// https://github.com/node-ffi/node-ffi/issues/632
// const ffi = require("ffi");

// ffi-cross or ffi-napi works, but ffi-napi is more popular
// https://github.com/ffi-cross/js-ffi-cross
// const ffi = require("ffi-cross");
// https://github.com/node-ffi-napi/node-ffi-napi
const ffi = require("ffi-napi");

const winmm = ffi.Library("winmm", {
  // https://learn.microsoft.com/en-us/previous-versions//dd757161(v=vs.85)
  mciSendStringA: ["int32", ["string", "string", "int32", "uint32"]],
});
// 292 MCIERR_MISSING_DEVICE_NAME if use mciSendStringW
// Maybe mciSendStringW needs to use wide string or utf8 string
// https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-basic-6/aa228215(v=vs.60)?redirectedfrom=MSDN
// https://learn.microsoft.com/en-us/windows/win32/multimedia/general-mci-errors
console.info(winmm.mciSendStringA('play "music.mid" wait', null, 0, null));
