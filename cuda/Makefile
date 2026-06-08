# Makefile — CUDA MLP Library for NCA Optimizer Benchmark
#
# GTX 1650 Max-Q = Turing = compute capability 7.5
# Produces libmlp_cuda.so for Python ctypes

NVCC       ?= nvcc
CUDA_ARCH  ?= sm_75
ARCH       = -arch=$(CUDA_ARCH)
NVCCFLAGS  = -O3 -std=c++17 -Xcompiler -fPIC -lineinfo
LDFLAGS    = -shared
LDLIBS     = -lcublas -lcurand
TARGET_MLP = libmlp_cuda.so
SRC_MLP    = mlp_cuda.cu
TARGET_CNN = libcnn_cuda.so
SRC_CNN    = cnn_cuda.cu

.PHONY: all clean test

all: $(TARGET_MLP) $(TARGET_CNN)

$(TARGET_MLP): $(SRC_MLP) mlp_cuda.h
	$(NVCC) $(ARCH) $(NVCCFLAGS) $(LDFLAGS) -o $@ $< $(LDLIBS)
	@echo "Built $(TARGET_MLP) successfully."

$(TARGET_CNN): $(SRC_CNN) cnn_cuda.h
	$(NVCC) $(ARCH) $(NVCCFLAGS) $(LDFLAGS) -o $@ $< $(LDLIBS)
	@echo "Built $(TARGET_CNN) successfully."

clean:
	rm -f $(TARGET_MLP) $(TARGET_CNN)

test: all
	@echo "Running quick smoke test..."
	python3 -c "import ctypes, pathlib; [ctypes.CDLL(str(pathlib.Path(p).resolve())) for p in ('./$(TARGET_MLP)', './$(TARGET_CNN)')]; print('CUDA libraries loaded OK')"
