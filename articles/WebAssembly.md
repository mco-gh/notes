WebAssembly

# WebAssembly

WebAssembly 1.0 has shipped in 4 major browser engines.  ![](../_resources/72f2de030367630ccab392261b0606eb.png)  ![](../_resources/c2db74e46cc2e22f2e94ab257c5f49fc.png)  ![](../_resources/c773c6f486abb6d16927726ce1e560a2.png)  ![](../_resources/dc9e990192d1d9005c6486ead71b5c6c.png)  ​[Learn more](http://webassembly.org/roadmap/)

WebAssembly (abbreviated *Wasm*) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.

Developer reference documentation for Wasm can be found on [MDN's WebAssembly pages](https://developer.mozilla.org/en-US/docs/WebAssembly). The open standards for WebAssembly are developed in a [W3C Community Group](https://www.w3.org/community/webassembly/) (that includes representatives from all major browsers) as well as a [W3C Working Group](https://www.w3.org/wasm/).

### Efficient and fast

The Wasm [stack machine](http://webassembly.org/docs/semantics/) is designed to be encoded in a size- and load-time-efficient [binary format](http://webassembly.org/docs/binary-encoding/). WebAssembly aims to execute at native speed by taking advantage of [common hardware capabilities](http://webassembly.org/docs/portability/#assumptions-for-efficient-execution) available on a wide range of platforms.

### Safe

WebAssembly describes a memory-safe, sandboxed [execution environment](http://webassembly.org/docs/semantics/#linear-memory) that may even be implemented inside existing JavaScript virtual machines. When [embedded in the web](http://webassembly.org/docs/web/), WebAssembly will enforce the same-origin and permissions security policies of the browser.

### Open and debuggable

WebAssembly is designed to be pretty-printed in a [textual format](http://webassembly.org/docs/text-format/) for debugging, testing, experimenting, optimizing, learning, teaching, and writing programs by hand. The textual format will be used when [viewing the source](http://webassembly.org/docs/faq/#will-webassembly-support-view-source-on-the-web) of Wasm modules on the web.

### Part of the open web platform

WebAssembly is designed to maintain the versionless, feature-tested, and backwards-compatible [nature of the web](http://webassembly.org/docs/web/). WebAssembly modules will be able to call into and out of the JavaScript context and access browser functionality through the same Web APIs accessible from JavaScript. WebAssembly also supports [non-web](http://webassembly.org/docs/non-web/) embeddings.

![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[< 1 min to Spreed]()