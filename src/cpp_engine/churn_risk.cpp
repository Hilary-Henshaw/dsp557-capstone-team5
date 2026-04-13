// build command: 
//g++ -shared -fPIC -std=c++17 -o src/cpp_engine/libchurn_risk.dylib src/cpp_engine/churn_risk.cpp

#include <cmath>

extern "C" {

const char* churn_risk_band(double prob) {
    if (std::isnan(prob)) {
        return "Unknown";
    }
    if (prob >= 0.70) {
        return "High Risk";
    }
    if (prob >= 0.40) {
        return "Medium Risk";
    }
    return "Low Risk";
}

}  // extern "C"
