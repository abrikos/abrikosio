// Source - https://stackoverflow.com/a
// Posted by imqqmi
// Retrieved 2026-01-16, License - CC BY-SA 4.0

//setup.ts
import {RouterLinkStub, config } from "@vue/test-utils";

config.global.stubs = {
    RouterLink: RouterLinkStub,
}
