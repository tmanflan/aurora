#!/usr/bin/env python3
"""
Simple test script for Aurora's core functionality.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_aurora_basic():
    """Test basic Aurora functionality."""
    try:
        from aurora import QuantumCompressedAurora
        
        print("✅ Successfully imported QuantumCompressedAurora")
        
        # Test initialization
        aurora = QuantumCompressedAurora()
        print("✅ Successfully initialized Aurora")
        
        # Test code generation
        result = aurora.generate_code("def test")
        print(f"✅ Code generation works: {result[:50]}...")
        
        # Test training
        aurora.model.quantum_train("def example(): return 42")
        print("✅ Training functionality works")
        
        # Test serialization
        serialized = aurora.model.serialize()
        print(f"✅ Serialization works: {len(serialized)} bytes")
        
        aurora.stop()
        print("✅ All basic tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_aurora_basic()
    sys.exit(0 if success else 1)