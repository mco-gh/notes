indutny/fft.js

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='159'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1068' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftjs)FFT.js

[![68747470733a2f2f7365637572652e7472617669732d63692e6f72672f696e6475746e792f6666742e6a732e737667](../_resources/087bbac58300ac5d38e541f4c3d661f2.png)](http://travis-ci.org/indutny/fft.js)[![68747470733a2f2f62616467652e667572792e696f2f6a732f6666742e6a732e737667](../_resources/3ace90d6d28612bdb67c02c50692013d.png)](https://badge.fury.io/js/fft.js)

Implementation of Radix-4 FFT.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='160'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1072' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#usage)Usage

const  FFT  =  require('fft.js');const  f  =  new  FFT(4096);const  input  =  new  Array(4096);input.fill(0);const  out  =  f.createComplexArray();

If `data` has just real numbers as is the case when `toComplexArray` is used - real FFT may be run to compute it 25% faster:

const  realInput  =  new  Array(f.size);f.realTransform(out, realInput);

`realTransform` fills just the left half of the `out`, so if the full spectrum is needed (which is symmetric), do the following:

f.completeSpectrum(out);
If `data` on other hand is a complex array:
const  data  =  f.toComplexArray(input);f.transform(out, data);
Inverse fourier transform:
f.inverseTransform(data, out);

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='161'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1083' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#benchmarks)Benchmarks

	$ npm run bench
	===== table construction =====
	    fft.js x 1,426 ops/sec ±0.70% (93 runs sampled)
	  Fastest is fft.js
	===== transform size=2048 =====
	    fft.js x 35,153 ops/sec ±0.83% (94 runs sampled)
	    jensnockert x 5,037 ops/sec ±0.98% (91 runs sampled)
	    dsp.js x 23,143 ops/sec ±0.64% (96 runs sampled)
	    drom x 14,372 ops/sec ±0.76% (92 runs sampled)
	  Fastest is fft.js
	===== transform size=4096 =====
	    fft.js x 15,676 ops/sec ±0.76% (94 runs sampled)
	    jensnockert x 3,864 ops/sec ±1.02% (93 runs sampled)
	    dsp.js x 7,905 ops/sec ±0.50% (97 runs sampled)
	    drom x 6,718 ops/sec ±0.78% (96 runs sampled)
	  Fastest is fft.js
	===== transform size=8192 =====
	    fft.js x 6,896 ops/sec ±0.79% (96 runs sampled)
	    jensnockert x 1,193 ops/sec ±0.73% (94 runs sampled)
	    dsp.js x 2,300 ops/sec ±0.74% (95 runs sampled)
	    drom x 3,164 ops/sec ±0.67% (95 runs sampled)
	  Fastest is fft.js
	===== transform size=16384 =====
	    fft.js x 3,123 ops/sec ±0.84% (95 runs sampled)
	    jensnockert x 855 ops/sec ±1.02% (92 runs sampled)
	    dsp.js x 948 ops/sec ±0.70% (94 runs sampled)
	    drom x 1,428 ops/sec ±0.56% (93 runs sampled)
	  Fastest is fft.js
	===== realTransform size=2048 =====
	    fft.js x 47,511 ops/sec ±0.93% (91 runs sampled)
	    fourier-transform x 34,859 ops/sec ±0.77% (93 runs sampled)
	  Fastest is fft.js
	===== realTransform size=4096 =====
	    fft.js x 21,841 ops/sec ±0.70% (94 runs sampled)
	    fourier-transform x 16,135 ops/sec ±0.39% (93 runs sampled)
	  Fastest is fft.js
	===== realTransform size=8192 =====
	    fft.js x 9,665 ops/sec ±0.65% (95 runs sampled)
	    fourier-transform x 6,456 ops/sec ±0.83% (93 runs sampled)
	  Fastest is fft.js
	===== realTransform size=16384 =====
	    fft.js x 4,399 ops/sec ±0.82% (93 runs sampled)
	    fourier-transform x 2,745 ops/sec ±0.68% (94 runs sampled)
	  Fastest is fft.js

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='162'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1085' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#api-details)API Details

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='163'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1087' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#constructor)Constructor

const  FFT  =  require('fft.js');const  fft  =  new  FFT(size);
NOTE: `size` MUST be a power of two and MUST be bigger than 1.

If you are looking to find the nearest power of 2 given the size of your dataset, here is a [good tutorial](https://stackoverflow.com/questions/466204/rounding-up-to-next-power-of-2/466256#466256)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='164'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1092' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#inputoutput-formats-and-helper-methods)Input/Output formats and helper methods.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='165'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1094' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftcreatecomplexarray)`fft.createComplexArray()`

Create an array of size equal to `fft.size * 2`. This array contains `fft.size` complex numbers whose real and imaginary parts are interleaved like this:

const  complexArray  = [ real0, imaginary0, real1, imaginary1, ... ];

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='166'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1098' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#ffttocomplexarrayrealinput--optional--storage)`fft.toComplexArray(realInput, /* optional */ storage)`

Use provided `storage` or create a new complex array and fill all real slots with values from `realInput` array, and all imaginary slots with zeroes.

*NOTE: Always provide `storage` for better performance and to avoid extra time in Garbage Collection.*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='167'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1103' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftfromcomplexarraycomplexinput--optional--storage)`fft.fromComplexArray(complexInput, /* optional */ storage)`

Use provided `storage` or create an array of size `fft.size` and fill it with real values from the `complexInput`.

*NOTE: Imaginary values from `complexInput` are ignored. This is a convenience method.*

*NOTE: Always provide `storage` for better performance and to avoid extra time in Garbage Collection.*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='168'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1110' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftcompletespectrumspectrum)`fft.completeSpectrum(spectrum)`

Fill the right half of `spectrum` complex array (See:`fft.createComplexArray()`) with the complex conjugates of the left half:

for (every every `i` between 1  and (N  /  2  -  1))
spectrum[N  - i] = spectrum*[i]

*NOTE: This method may be used with `fft.realTransform()` if full output is desired.*

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='169'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1116' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fft-methods)FFT Methods

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='170'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1118' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftrealtransformoutput-input)`fft.realTransform(output, input)`

Take array of real numbers `input` and perform FFT transformation on it, filling the left half of the `output` with the real part of the Fourier Transform's complex output (See:`fft.completeSpectrum()`).

*NOTE: Always use this method if the input for FFT transformation is real (has no imaginary parts). It is about 40% faster to do such transformation this way.*

*NOTE: `input` - real array of size `fft.size`, `output` - complex array (See:`fft.createComplexArray()`).*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='171'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1125' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#ffttransformoutput-input)`fft.transform(output, input)`

Perform transformation on complex `input` array and store results in the complex `output` array.

*NOTE: `input` and `output` are complex arrays (See:`fft.createComplexArray()`).*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='172'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1130' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#fftinversetransformoutput-input)`fft.inverseTransform(output, input)`

Perform inverse Fourier transform on complex `input` array and store results in the complex `output` array.

*NOTE: `input` and `output` are complex arrays (See:`fft.createComplexArray()`).*

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='173'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1135' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/indutny/fft.js/#license)LICENSE

This software is licensed under the MIT License.
Copyright Fedor Indutny, 2017.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.