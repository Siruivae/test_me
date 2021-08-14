#pad(array, pad_width, mode, **kwargs)
def zero_pad(X, pad):
    X_pad = np.pad(X, ((pad, pad), (pad, pad)), 'constant', constant_values=0)

    return X_pad


def conv_forward(A_prev, W, hparameters):  # A_prev上一层的输出，W是卷积核，b是bias偏置，hparameters是个字典，包含步长和填充数量
    (n_H_prev, n_W_prev) = A_prev.shape  # 图片的数量，高，宽，通道数
    (f, f) = W.shape  # 卷积核的高，宽，通道数，数量
    stride = hparameters['stride']  # 滑动步长
    pad = hparameters['pad']  # 填充数量

    n_H = 1 + int((n_H_prev + 2 * pad - f) / stride)  # 卷积后的高（int向下取整）
    n_W = 1 + int((n_W_prev + 2 * pad - f) / stride)  # 卷积后的宽

    Z = np.zeros((n_H, n_W))  # 初始化卷积后的输出Z
    A_prev_pad = zero_pad(A_prev, pad)  # 对上一层的输出A进行pedding填充

    #for i in range(m):  # 第i张图片
        # a_prev_pad = A_prev_pad[i] #第1张图
        for h in range(n_H):  # 先固定图像高
            for w in range(n_W):  # 高度不变，宽度变，即向右滑动，得到卷积后的固定行的列。
                #for c in range(n_C):  # 第一个卷积核

                    vert_start = h * stride  # 滑动窗口的起始行（高）
                    vert_end = vert_start + f  # 滑动窗口的结束行（高）
                    horiz_start = w * stride  # 滑动窗口的起始列（列）
                    horiz_end = horiz_start + f  # 滑动窗口的结束列（列）

                    a_slice_prev = A_prev_pad[vert_start:vert_end, horiz_start:horiz_end]  # 从第一张图切片出一个滑动窗口
                    # a_slice_prev = a_prev_pad[vert_start:vert_end,horiz_start:horiz_end,:] #从第一张图切片出一个滑动窗口
                    Z[h, w] = np.sum(
                        np.multiply(a_slice_prev, W[:, :]))  # 一块窗口的卷积运算，相当于前面的conv_single_step()

    assert (Z.shape == (n_H, n_W))

    cache = (A_prev, W, hparameters)
    return Z, cache


def conv_naive(x, ksize, padding=0, stride=1):
    # x = [b, h, w, in_c]
    h, w = x.shape
    kernel = np.random.rand(ksize, ksize)
    if padding > 0:
        pad_x = np.zeros((h+2*padding, w+2*padding))
        pad_x[padding:-padding,padding:-padding] = x

    out_h = (h+2*padding-ksize)//stride+1
    out_w = (w+2*padding-ksize)//stride+1
    out = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            roi_x = pad_x[i*stride:i*stride+ksize,j*stride:j*stride+ksize]
            # roi_x = [b, ksize, ksize, in_c] -> [b, ksize, ksize, in_c, out_c]
            # kernel = [ksize, ksize, in_c, out_c]
            # conv = [b, ksize, ksize, in_c, out_c] -> [b, 1, 1, out_c]
            conv = np.tile(np.expand_dims(roi_x, -1), (1,1,1,1))*kernel
            out[:,i,j,:] = np.squeeze(np.sum(conv, axis=(1,2,3), keepdims=True), axis=3)
    return out

def zero_pad(X, pad):
    X_pad = np.pad(X, ((pad, pad), (pad, pad)), 'constant', constant_values=0)
    return X_pad
def conv_naive(x, ksize, padding=0, stride=1):
    h, w = x.shape
    kernel = np.random.rand(ksize, ksize)
    '''if padding > 0:
        pad_x = np.zeros((h+2*padding, w+2*padding))
        pad_x[padding:-padding,padding:-padding] = x'''

    out_h = (h+2*padding-ksize)//stride+1
    out_w = (w+2*padding-ksize)//stride+1
    out = np.zeros((out_h, out_w))
    pad_x = zero_pad(x, padding)  # 对上一层的输出A进行pedding填充

    for i in range(out_h):
        for j in range(out_w):
            roi_x = pad_x[i*stride:i*stride+ksize,j*stride:j*stride+ksize]
            out[h, w] = np.sum(
                np.multiply(roi_x, kernel[:, :]))  # 一块窗口的卷积运算，相当于前面的conv_single_step()
    return out
def pad(x, pad):
    x_pad = np.pad(x, ((pad,pad), (pad, pad)), 'constant')
    return x_pad
def conv(x, ksize, padding = 0, stride=1):
    h,w =x.shape
    kernal = np.random.rand(ksize, ksize)
    o_h = (h - ksize + 2 * padding)//2 +1
    o_w = (w - ksize + 2 * padding) // 2 + 1
    out = np.zero(o_h, o_w)
    pad_x = pad(x, padding)

    for i in range(o_h):
        for j in range(o_w):
            roi_x = pad_x[i*stride:i*stride+ksize, j*stride:j*stride+ksize]
            out[i, j] = np.sum(
                np.multiply(roi_x, kernal[:, :]))
    return out