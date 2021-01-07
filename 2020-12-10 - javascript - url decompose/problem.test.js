// Estacionamento de cursores: |


const decomposeUrl = rawUrl => {
    let result = {
        scheme: null,
        ipAdress: null,
        netLoc: null,
        folderTree: null,
        targetFile: null,
        argumentsFile: null,
    }
    if (!rawUrl) {
        return result
    }

    const url = rawUrl[rawUrl.length - 1] === '/' ? rawUrl : `${rawUrl}/`
    const schemeAndRest = url.split("://")
    const scheme = schemeAndRest[0]
    const location = schemeAndRest[1]
    const splitLocation = location.split('/')
    const folderTree = splitLocation.slice(1, splitLocation.length - 2)
    result.scheme = scheme
    result.folderTree = folderTree
    result.targetFile = splitLocation[splitLocation.length - 2]

    if (/\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}/.test(splitLocation[0])) {
        result.ipAdress = splitLocation[0]
    } else {
        result.netLoc = splitLocation[0]
    }

    return result
}

test('return targetFile address', () => {
    expect(decomposeUrl('http://example.com/folder1/folder2/index.html').targetFile).toEqual('index.html');
});

test('return folderTree address', () => {
    expect(decomposeUrl('http://example.com/folder1/folder2/index.html').folderTree).toEqual(['folder1', 'folder2']);
});

test('return netLoc address', () => {
    expect(decomposeUrl('http://example.com').netLoc).toEqual('example.com');
});

test('return IP address', () => {
    expect(decomposeUrl('http://127.0.0.1').ipAdress).toEqual('127.0.0.1');
});

test('return https scheme', () => {
    const returnedURL = decomposeUrl('https://test.com')

    expect(returnedURL.scheme).toEqual('https');
});

test('return http scheme', () => {

    expect(decomposeUrl('http://test.com').scheme).toEqual('http')
});

test('return url object', () => {
    const result = decomposeUrl('')

    const properties = [
        "scheme",
        "ipAdress",
        "netLoc",
        "folderTree",
        "targetFile",
        "argumentsFile"
    ]
    expect(Object.keys(result)).toEqual(properties)
});


