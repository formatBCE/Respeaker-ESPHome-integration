#pragma once

#include <cstdint>

namespace esphome::incubator_timer {

// The fields of voice_assistant::Timer that the device packages read.
struct Timer {
  uint32_t total_seconds{0};
  uint32_t seconds_left{0};
};

}  // namespace esphome::incubator_timer
