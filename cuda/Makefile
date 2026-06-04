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
TARGET     = libmlp_cuda.so
SRC        = mlp_cuda.cu

.PHONY: all clean test

all: $(TARGET)

$(TARGET): $(SRC) mlp_cuda.h
	$(NVCC) $(ARCH) $(NVCCFLAGS) $(LDFLAGS) -o $@ $< $(LDLIBS)
	@echo "Built $(TARGET) successfully."

clean:
	rm -f $(TARGET)

test: $(TARGET)
	@echo "Running quick smoke test..."
	python3 -c "import ctypes; lib = ctypes.CDLL('./$(TARGET)'); print('Library loaded OK')"
