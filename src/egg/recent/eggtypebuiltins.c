
/* Generated data (by glib-mkenums) */

#include "egg-recent.h"
#include "egg-recent-item.h"
#include "egg-recent-model.h"
#include "egg-recent-view.h"
#include "egg-recent-view-bonobo.h"
#include "egg-recent-view-gtk.h"

/* enumerations from "egg-recent-model.h" */
GType
egg_recent_model_sort_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GEnumValue values[] = {
      { EGG_RECENT_MODEL_SORT_MRU, "EGG_RECENT_MODEL_SORT_MRU", "mru" },
      { EGG_RECENT_MODEL_SORT_LRU, "EGG_RECENT_MODEL_SORT_LRU", "lru" },
      { EGG_RECENT_MODEL_SORT_NONE, "EGG_RECENT_MODEL_SORT_NONE", "none" },
      { 0, NULL, NULL }
    };
    etype = g_enum_register_static ("EggRecentModelSort", values);
  }
  return etype;
}

/* Generated data ends here */

