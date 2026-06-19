import pandas as pd, seaborn as sb, matplotlib.pyplot as mpl

def plot_protein_length(df):
    sb.set_theme(style="darkgrid")
    mpl.figure(figsize=(12,6))
    
    sb.barplot(data=df, 
               x = "gene", 
               y = "protein_length",
               palette=sb.color_palette("flare", 5) + sb.color_palette("crest", 5)
            )
    
    mpl.title("Protein Length by Gene")
    mpl.xlabel("Gene")
    mpl.ylabel("Protein Length (aa)")
    # mpl.xticks(rotation=45)

    mpl.tight_layout()

    mpl.savefig('./results/figures/protein_length.png',dpi=300)

    mpl.close()
    
def plot_instability_index(df):
    sb.set_theme(style="darkgrid")
    mpl.figure(figsize=(12,6))
    
    sb.boxplot(data=df, 
               x = "group", 
               y = "instability_index",
               hue="group",
               palette={
                   "disease":sb.color_palette("flare")[4],
                   "control":sb.color_palette("crest")[4]
               }
            )
    
    mpl.title("Instability Index by Group")
    mpl.xlabel("Group")
    mpl.ylabel("Instability Index")
    # mpl.xticks(rotation=45)

    mpl.tight_layout()

    mpl.savefig('./results/figures/instability_index.png',dpi=300)

    mpl.close()
    
def plot_gravy(df):
    sb.set_theme(style="darkgrid")
    mpl.figure(figsize=(12,6))
    
    sb.boxplot(data=df, 
               x = "group", 
               y = "gravy",
               hue="group",
               palette={
                   "disease":sb.color_palette("flare")[4],
                   "control":sb.color_palette("crest")[4]
               }
            )
    
    mpl.title("GRAVY by Group")
    mpl.xlabel("Group")
    mpl.ylabel("GRAVY")
    # mpl.xticks(rotation=45)

    mpl.tight_layout()

    mpl.savefig('./results/figures/gravy.png',dpi=300)

    mpl.close()
    
def plot_aromaticity(df):
    sb.set_theme(style="darkgrid")
    mpl.figure(figsize=(12,6))
    
    sb.boxplot(data=df, 
               x = "group", 
               y = "aromaticity",
               hue="group",
               palette={
                   "disease":sb.color_palette("flare")[4],
                   "control":sb.color_palette("crest")[4]
               }
            )
    
    mpl.title("Aromaticity by Group")
    mpl.xlabel("Group")
    mpl.ylabel("Aromaticity")
    # mpl.xticks(rotation=45)

    mpl.tight_layout()

    mpl.savefig('./results/figures/aromaticity.png',dpi=300)

    mpl.close()
    
def plot_amino_acid_heatmap(df):

    aa_cols = [
        "A","C","D","E","F","G","H","I","K","L",
        "M","N","P","Q","R","S","T","V","W","Y"
    ]

    heatmap_df = df.set_index("gene")[aa_cols]

    heatmap_df = heatmap_df.div(
        df.set_index("gene")["protein_length"],
        axis=0
    )

    sb.set_theme(style="dark")

    mpl.figure(figsize=(12,6))

    sb.heatmap(
        heatmap_df,
        cmap="mako",
        annot=False
    )

    mpl.title("Normalaized Amino Acid Composition Heatmap")
    mpl.xlabel("Amino Acid")
    mpl.ylabel("Protein")

    mpl.tight_layout()

    mpl.savefig("./results/figures/normalized_aa_heatmap.png",dpi=300)

    mpl.close()
    
def plot_correlation_matrix(df):
    
    numeric_cols = [
    "protein_length",
    "molecular_weight",
    "isoelectric_point",
    "aromaticity",
    "instability_index",
    "gravy",
    "alpha_structure_fraction",
    "turn_structure_fraction",
    "beta_structure_fraction"
]

    sb.set_theme(style="dark")

    mpl.figure(figsize=(10,8))

    corr = df[numeric_cols].corr()

    sb.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )

    mpl.title("Correlation Matrix of Protein Properties")

    mpl.tight_layout()

    mpl.savefig("./results/figures/correlation_matrix.png",dpi=300)

    mpl.close()